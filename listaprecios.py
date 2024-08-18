# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Listaprecios(models.Model):
    _name = 'materiales.listaprecios'

    fecha = fields.Date(string='Fecha', default=fields.Date.context_today, readonly=True)
    proveedor_id = fields.Many2one('materiales.proveedor', string='Proveedor', required=True)
    producto_id = fields.Many2one('materiales.productos', string='Producto')
    aplicado = fields.Boolean(string='Aplicado', default=False)
    line_ids = fields.One2many('materiales.listaprecios.line', 'listaprecios_id', string='Detalles de Lista de Precios')

    @api.multi
    def actualizar_precio(self):
        self.ensure_one()
        if not self.aplicado:
            for line in self.line_ids:
                if line.nuevo_precio:
                    line.producto_id.write({'valor_actual': line.nuevo_precio})
            self.aplicado = True
            self.sync_catalogo()

    @api.onchange('proveedor_id')
    def _onchange_proveedor_id(self):
        # Filtrar los productos basados en el proveedor seleccionado
        return {'domain': {'producto_id': [('proveedor_id', '=', self.proveedor_id.id)]}}

    @api.model
    def create(self, vals):
        record = super(Listaprecios, self).create(vals)
        record.sync_catalogo()
        return record

    @api.multi
    def write(self, vals):
        res = super(Listaprecios, self).write(vals)
        self.sync_catalogo()
        return res

    @api.multi
    def sync_catalogo(self):
        catalogo_model = self.env['catalogo.productos']
        productos = self.env['materiales.productos'].search([])
        for producto in productos:
            catalogo_producto = catalogo_model.search([('clave', '=', producto.clave)], limit=1)
            if catalogo_producto:
                catalogo_producto.write({
                    'nombre': producto.name,
                    'precio_actual': producto.valor_actual,
                    'categoria': producto.tipo_producto
                })
            else:
                catalogo_model.create({
                    'clave': producto.clave,
                    'nombre': producto.name,
                    'precio_actual': producto.valor_actual,
                    'categoria': producto.tipo_producto
                })

class Detalleprecios(models.Model):
    _name = 'materiales.listaprecios.line'

    listaprecios_id = fields.Many2one('materiales.listaprecios', string='Lista de Precios')
    producto_id = fields.Many2one('materiales.productos', string='Producto')
    clave = fields.Char(string='Clave')
    nombre = fields.Char(string='Nombre')
    precio_actual = fields.Float(string='Precio Actual')
    nuevo_precio = fields.Float(string='Nuevo Precio')

    @api.onchange('producto_id')
    def _onchange_producto_id(self):
        if self.producto_id:
            self.clave = self.producto_id.clave
            self.nombre = self.producto_id.name
            self.precio_actual = self.producto_id.valor_actual


class CatalogoProductos(models.Model):
    _name = 'catalogo.productos'
    _description = 'Catálogo de Productos'
    _rec_name = 'nombre'

    clave = fields.Char(string='Clave', readonly=True)
    nombre = fields.Char(string='Nombre', readonly=True)
    precio_actual = fields.Float(string='Precio Actual', readonly=True)
    categoria = fields.Char(string='Categoría', readonly=True)
