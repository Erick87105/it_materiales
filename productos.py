# -- coding: utf-8 --
from openerp import models, fields

class Productos(models.Model):
    _name = 'materiales.productos'

    foto = fields.Binary(string='Foto del Producto') 
    name = fields.Char(string='Nombre del Producto')
    marca = fields.Char(string='Marca')
    modelo = fields.Char(string='Modelo')
    serie = fields.Char(string='Identificación de Serie')
    TIPO_PRODUCTO = [
        ('tipo1', 'Tipo 1'),
        ('tipo2', 'Tipo 2'),
        ('tipo3', 'Tipo 3'),
    ]


    tipo_producto = fields.Selection(TIPO_PRODUCTO, string='Tipo de Producto')
    valor_actual = fields.Float(string='Valor Actual')
    activo = fields.Boolean(string='Activo')
    estatus = fields.Char(string='Estado')
    anos_vida_util = fields.Integer(string='Años de Vida Útil')
    observaciones = fields.Text(string='Observaciones')
    descripcion = fields.Text(string='Descripción')
    
