# -*- coding: utf-8 -*-
from openerp import models, fields, api

class CatalogoProductos(models.Model):
    _name = 'catalogo.productos'

    clave = fields.Char(string='Clave', compute='_compute_clave')
    nombre = fields.Char(string='Nombre', compute='_compute_nombre')
    precio_actual = fields.Float(string='Precio Actual', compute='_compute_precio_actual')
    categoria = fields.Char(string='Categoría', compute='_compute_categoria')

    @api.depends('clave', 'nombre', 'precio_actual', 'categoria')
    def _compute_clave(self):
        for record in self:
            record.clave = record.producto_id.clave if record.producto_id else ''

    @api.depends('clave', 'nombre', 'precio_actual', 'categoria')
    def _compute_nombre(self):
        for record in self:
            record.nombre = record.producto_id.name if record.producto_id else ''

    @api.depends('clave', 'nombre', 'precio_actual', 'categoria')
    def _compute_precio_actual(self):
        for record in self:
            record.precio_actual = record.producto_id.valor_actual if record.producto_id else 0.0

    @api.depends('clave', 'nombre', 'precio_actual', 'categoria')
    def _compute_categoria(self):
        for record in self:
            record.categoria = record.producto_id.tipo_producto if record.producto_id else ''

