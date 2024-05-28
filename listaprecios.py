# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Listaprecios(models.Model):
    _name = 'materiales.listaprecios'

    fecha = fields.Date(string='Fecha', default=fields.Date.context_today, readonly=True)
    proveedor_id = fields.Many2one('res.partner', string='Proveedor', required=True)
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

class Detalleprecios(models.Model):
    _name = 'materiales.listaprecios.line'

    listaprecios_id = fields.Many2one('materiales.listaprecios', string='Lista de Precios')
    producto_id = fields.Many2one('materiales.productos', string='Producto')
    clave = fields.Char(string='Clave')
    nombre = fields.Char(string='Nombre')
    precio_actual = fields.Float(string='Precio Actual')
    nuevo_precio = fields.Float(string='Nuevo Precio')
