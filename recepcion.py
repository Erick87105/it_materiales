
# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.exceptions import ValidationError
from datetime import datetime
import difflib  # Necesario para la búsqueda de similitud
import logging

_logger = logging.getLogger(__name__)

class Recepcion(models.Model):
    _name = 'materiales.recepcion'

    name = fields.Char(string='Folio', readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('Foliorecepciones'))
    fecha = fields.Datetime(string='Fecha y hora', default=fields.Datetime.now, readonly=True)
    status = fields.Selection([('creado', 'Creado'), ('aplicado', 'Aplicado'), ('cancelado', 'Cancelado')], string='Estado', default='creado')
    observaciones = fields.Text(string='Observaciones')
    ubicacion_recepcion = fields.Selection([('bodega', 'Bodega Materiales'), ('otros', 'Otros')], string='Ubicación de Recepción', required=True, default='bodega')
    detalle_ids = fields.One2many('materiales.detallerec', 'recepcion_id', string='Detalles de Recepción')
    compra_ids = fields.Many2many('materiales.comprados', string='Compras', domain="[('status', '=', 'pedido')]")
    factura_ids = fields.Many2many('materiales.factura', string='Facturas')

    @api.model
    def create(self, vals):
        if 'name' not in vals:
            vals['name'] = self.env['ir.sequence'].next_by_code('Foliorecepciones')
        return super(Recepcion, self).create(vals)

    def action_aplicar(self):
        self.validar_costos()
        self.validar_factura()
        self.write({'status': 'aplicado'})
        if self.compra_ids:
            self.compra_ids.write({'status': 'recibido'})

    def action_cancelar(self):
        self.write({'status': 'cancelado'})

    @api.onchange('compra_ids')
    def _onchange_compra_ids(self):
        if self.compra_ids:
            detalle_data = []
            for compra in self.compra_ids:
                for detalle in compra.compra_detalle_ids:
                    detalle_data.append((0, 0, {
                        'producto': detalle.producto,
                        'cantidad': detalle.cantidad,
                        'costo_estimado': detalle.costo_estimado,
                        'compra_id': compra.id,
                    }))
            self.detalle_ids = detalle_data

    def validar_costos(self):
        param_obj = self.env['ir.config_parameter']
        umbral = float(param_obj.sudo().get_param('DIFERENCIA_COSTO_PERMITIDA', '10'))

        for detalle in self.detalle_ids:
            if detalle.costo_estimado:
                diferencia = abs(detalle.costo_real - detalle.costo_estimado) / detalle.costo_estimado * 100
                if diferencia > umbral:
                    raise ValidationError(
                        u'El costo real de {0} excede el umbral permitido de {1}%. Revise la factura o contacte al proveedor.'.format(
                            detalle.producto, umbral))

    def validar_factura(self):
        for factura in self.factura_ids:
            total_estimado = sum(detalle.cantidad * detalle.costo_estimado for detalle in factura.recepcion_ids.mapped('detalle_ids'))
            if factura.monto_total > total_estimado * 1.10:  # Umbral del 10%
                raise ValidationError(
                    u'El monto total de la factura excede el 110% del costo estimado. Verifique los datos antes de continuar.')

    def crear_factura(self):
        factura_vals = {
            'numero_factura': 'Folio por Definir',
            'fecha_emision': fields.Date.context_today(self),
            'proveedor_id': False,  # Selecciona el proveedor más adelante
            'detalles_factura': [],
        }
        for detalle in self.detalle_ids:
            factura_vals['detalles_factura'].append((0, 0, {
                'producto_id': detalle.producto_id.id,
                'cantidad': detalle.cantidad,
                'precio_unitario': 0.0,  # Precio por definir
            }))
        self.env['materiales.factura'].create(factura_vals)

    @api.multi
    def action_validar_recepcion(self):
        # Verificar cada producto en los detalles de recepción
        for detalle in self.detalle_ids:
            producto_existente = self.buscar_producto_similar(detalle.producto)
            
            if not producto_existente:
                # Registrar un nuevo producto si no existe en el sistema
                nuevo_producto = self.registrar_nuevo_producto(detalle)
                try:
                    creado_producto = self.env['materiales.productos'].create(nuevo_producto)
                    _logger.info('Nuevo producto creado: %s', creado_producto.name)
                except Exception as e:
                    _logger.error('Error al crear el producto: %s', e)
            else:
                _logger.info('Producto similar encontrado: %s', producto_existente.name)

        # Cambiar el estado de las compras asociadas a "recibido"
        if self.compra_ids:
            self.compra_ids.write({'status': 'recibido'})
        
        # Marcar la recepción como "aplicada"
        self.write({'status': 'aplicado'})

        

    def buscar_producto_similar(self, producto_nombre):
        productos = self.env['materiales.productos'].search([])
        for producto in productos:
            similitud = difflib.SequenceMatcher(None, producto.name, producto_nombre).ratio()
            if similitud > 0.8:  # Ajustable
                return producto
        return False

    def registrar_nuevo_producto(self, detalle):
        return {
            'name': detalle.producto,
            'marca': detalle.marca,
            'modelo': detalle.modelo,
            'serie': detalle.serie,
            'categoria_id': detalle.categoria_id.id,  # Asegúrate de que estos campos existan
            'subcategoria_id': detalle.subcategoria_id.id,
            'cantidad': detalle.cantidad,
            'valor_actual': detalle.costo_estimado,
            'anos_vida_util': detalle.anos_vida_util,
            'depreciacion_anual': detalle.depreciacion_anual,
            'activo': True,
        }
        
class DepreciacionCategoria(models.Model):
    _name = 'depreciacion.categoria'
    _description = 'Categorías de Depreciación'

    nombre = fields.Char(string='Nombre de la Categoría', required=True)
    descripcion = fields.Text(string='Descripción de la Categoría')
    subcategoria_ids = fields.One2many('depreciacion.subcategoria', 'categoria_id', string='Subcategorías')


class DepreciacionSubcategoria(models.Model):
    _name = 'depreciacion.subcategoria'
    _description = 'Subcategorías de Depreciación'

    nombre = fields.Char(string='Nombre de la Subcategoría', required=True)
    descripcion = fields.Text(string='Descripción de la Subcategoría')
    anos_vida_util = fields.Integer(string='Años de Vida Útil', required=True)
    depreciacion_anual = fields.Float(string='Porcentaje de Depreciación Anual (%)', required=True)
    categoria_id = fields.Many2one('depreciacion.categoria', string='Categoría', ondelete='cascade', required=True)

class Detallerec(models.Model):
    _name = 'materiales.detallerec'

    recepcion_id = fields.Many2one('materiales.recepcion', string='Recepción')
    producto = fields.Char(string='Producto')
    marca = fields.Char(string='Marca')
    modelo = fields.Char(string='Modelo')
    serie = fields.Char(string='Serie')

    # Cambiar a Many2one para relacionar con el modelo de categoría
    categoria_id = fields.Many2one('depreciacion.categoria', string='Categoría', required=True)

    # Cambiar a Many2one para relacionar con el modelo de subcategoría
    subcategoria_id = fields.Many2one('depreciacion.subcategoria', string='Subcategoría', domain="[('categoria_id', '=', categoria_id)]", required=True)

    cantidad = fields.Integer(string='Cantidad')
    costo_estimado = fields.Float(string='Costo Estimado')
    costo_real = fields.Float(string='Costo Real')

    # Estos campos se llenarán automáticamente
    anos_vida_util = fields.Integer(string='Años de Vida Útil', compute='_compute_depreciacion', store=True)
    depreciacion_anual = fields.Float(string='Depreciación Anual (%)', compute='_compute_depreciacion', store=True)

    @api.depends('subcategoria_id')
    def _compute_depreciacion(self):
        for record in self:
            if record.subcategoria_id:
                record.anos_vida_util = record.subcategoria_id.anos_vida_util
                record.depreciacion_anual = record.subcategoria_id.depreciacion_anual
            else:
                record.anos_vida_util = 0
                record.depreciacion_anual = 0

    @api.onchange('categoria_id')
    def _onchange_categoria_id(self):
        # Limpiar la subcategoría al cambiar la categoría
        self.subcategoria_id = False


class Factura(models.Model):
    _name = 'materiales.factura'

    recepcion_ids = fields.Many2many('materiales.recepcion', string='Recepciones')
    numero_factura = fields.Char(string='Número de Factura', required=True)
    rfc = fields.Char(string='RFC')
    proveedor_id = fields.Many2one('materiales.proveedor', string='Proveedor', required=True)
    fecha_emision = fields.Date(string='Fecha de Emisión', default=fields.Date.context_today, required=True)
    monto_total = fields.Float(string='Monto Total', compute='_compute_monto_total')
    detalles_factura = fields.One2many('materiales.detallefactura', 'factura_id', string='Detalles de Factura')

    @api.depends('detalles_factura.subtotal')
    def _compute_monto_total(self):
        for factura in self:
            factura.monto_total = sum(detalle.subtotal for detalle in factura.detalles_factura)

    @api.onchange('recepcion_ids')
    def _onchange_recepcion_ids(self):
        if self.recepcion_ids:
            detalle_data = []
            for recepcion in self.recepcion_ids:
                for detalle in recepcion.detalle_ids:
                    detalle_data.append((0, 0, {
                        'producto_id': detalle.producto_id.id,
                        'cantidad': detalle.cantidad,
                        'precio_unitario': detalle.costo_real,
                    }))
            self.detalles_factura = detalle_data
            self._compute_monto_total()


class DetalleFactura(models.Model):
    _name = 'materiales.detallefactura'

    factura_id = fields.Many2one('materiales.factura', string='Factura', required=True)
    producto_id = fields.Many2one('materiales.productos', string='Producto', required=True)
    cantidad = fields.Integer(string='Cantidad', required=True)
    precio_unitario = fields.Float(string='Precio Unitario', required=True)
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)

    @api.depends('cantidad', 'precio_unitario')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.cantidad * record.precio_unitario
