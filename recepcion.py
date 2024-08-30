
# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.exceptions import ValidationError
from datetime import datetime
import difflib  # Necesario para la búsqueda de similitud

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
        vals['name'] = self.env['ir.sequence'].next_by_code('Foliorecepciones')
        return super(Recepcion, self).create(vals)

    @api.multi
    def action_aplicar(self):
        self.validar_costos()
        self.validar_factura()
        self.write({'status': 'aplicado'})
        if self.compra_ids:
            self.compra_ids.write({'status': 'recibido'})

    @api.multi
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

    @api.multi
    def validar_costos(self):
        param_obj = self.env['materiales.parametros']
        umbral = float(param_obj.get_param('DIFERENCIA_COSTO_PERMITIDA', '10'))
        
        for detalle in self.detalle_ids:
            diferencia = abs(detalle.costo_real - detalle.costo_estimado) / detalle.costo_estimado * 100
            if diferencia > umbral:
                raise ValidationError(
                    u'El costo real de {0} excede el umbral permitido de {1}%. Revise la factura o contacte al proveedor.'.format(
                        detalle.producto, umbral))

    @api.multi
    def validar_factura(self):
        for factura in self.factura_ids:
            total_estimado = sum(detalle.cantidad * detalle.costo_estimado for detalle in factura.recepcion_ids.mapped('detalle_ids'))
            if factura.monto_total > total_estimado * 1.10:  # Umbral del 10%
                raise ValidationError(
                    u'El monto total de la factura excede el 110% del costo estimado. Verifique los datos antes de continuar.')

    @api.multi
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

    # Nuevas adiciones:
    # @api.multi
    # def action_validar_recepcion(self):
    #     # Verificar cada producto en los detalles de recepción
    #     for detalle in self.detalle_ids:
    #         producto_existente = self.buscar_producto_similar(detalle.producto)
            
    #         if not producto_existente:
    #             # Registrar un nuevo producto si no existe en el sistema
    #             nuevo_producto = self.registrar_nuevo_producto(detalle)
    #             self.env['materiales.productos'].create(nuevo_producto)
    #         else:
    #             # Producto ya existe, puedes actualizar la cantidad o cualquier otro campo aquí si es necesario.
    #             pass
    #     # Marcar recepción como aplicada
    #     self.write({'status': 'aplicado'})
    @api.multi
    def action_validar_recepcion(self):
        # Recorrer cada detalle de la recepción
        for detalle in self.detalle_ids:
            # Buscar un producto similar en la base de datos
            producto_existente = self.buscar_producto_similar(detalle.producto)
            
            if not producto_existente:
                # Si no se encuentra un producto similar, crear uno nuevo
                nuevo_producto = self.registrar_nuevo_producto(detalle)
                creado_producto = self.env['materiales.productos'].create(nuevo_producto)
                if creado_producto:
                    _logger.info('Nuevo producto creado: %s', creado_producto.name)
            else:
                _logger.info('Producto similar encontrado: %s', producto_existente.name)
                # Si se encuentra un producto similar, puedes realizar alguna acción adicional aquí
                # como actualizar cantidades, etc.

        # Marcar la recepción como "aplicado" después de la validación
        self.write({'status': 'aplicado'})

    
    def buscar_producto_similar(self, producto_nombre):
        # Buscar productos similares en la base de datos
        productos = self.env['materiales.productos'].search([])
        for producto in productos:
            similitud = difflib.SequenceMatcher(None, producto.name, producto_nombre).ratio()
            if similitud > 0.8:  # Puedes ajustar este valor según la similitud que desees permitir
                return producto
        return False
    
    def registrar_nuevo_producto(self, detalle):
        return {
            'name': detalle.producto,
            'marca': detalle.marca,
            'modelo': detalle.modelo,
            'serie': detalle.serie,
            'categoria': detalle.categoria,
            'subcategoria': detalle.subcategoria,
            'cantidad': detalle.cantidad,
            'valor_actual': detalle.costo_estimado,
            'anos_vida_util': detalle.anos_vida_util,
            'depreciacion_anual': detalle.depreciacion_anual,
            'activo': True,
        }

class Detallerec(models.Model):
    _name = 'materiales.detallerec'

    recepcion_id = fields.Many2one('materiales.recepcion', string='Recepción')
    producto = fields.Char(string='Producto')
    marca = fields.Char(string='Marca')
    modelo = fields.Char(string='Modelo')
    serie = fields.Char(string='Serie')
    categoria = fields.Selection([('inmuebles', 'Inmuebles'), ('muebles', 'Muebles')], string='Categoría')
    subcategoria = fields.Selection([('viviendas', 'Viviendas'), ('edificios', 'Edificios')], string='Subcategoría')
    cantidad = fields.Integer(string='Cantidad')
    costo_estimado = fields.Float(string='Costo Estimado')
    costo_real = fields.Float(string='Costo Real')
    compra_id = fields.Many2one('materiales.comprados', string='Compra Asociada')

class Factura(models.Model):
    _name = 'materiales.factura'

    recepcion_ids = fields.Many2many('materiales.recepcion', string='Recepciones', 
                                     help="Selecciona una o más recepciones para esta factura.")
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
                        'precio_unitario': detalle.costo_real,  # Asumiendo que el costo real es el precio unitario
                    }))
            self.detalles_factura = detalle_data
            self._compute_monto_total()  # Asegurarse de que el monto total esté actualizado

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
