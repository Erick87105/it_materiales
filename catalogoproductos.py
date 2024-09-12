# -*- coding: utf-8 -*-
from openerp import models, fields, api

class CatalogoProductos(models.Model):
    _name = 'catalogo.productos'

    clave = fields.Char(string='Clave', readonly=True)
    nombre = fields.Char(string='Nombre', readonly=True)
    precio_actual = fields.Float(string='Precio Actual', readonly=True)
    categoria = fields.Char(string='Categoría', readonly=True)

