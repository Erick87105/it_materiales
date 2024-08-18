# -*- coding: utf-8 -*-
from openerp import models, fields, api

class CatalogoProductos(models.Model):
    _name = 'catalogo.productos'

    clave = fields.Char(string='Clave')
    nombre = fields.Char(string='Nombre')
    precio_actual = fields.Float(string='Precio Actual')
    categoria = fields.Char(string='Categoría')

