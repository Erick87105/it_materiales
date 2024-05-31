# -*- coding: utf-8 -*-

from openerp import models, fields

class Proveedor(models.Model):
    _name = 'materiales.proveedor'
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'El nombre de la empresa ya existe.')
    ]

    name = fields.Char(string='Nombre de la Empresa', required=True)
    domicilio = fields.Char(string='Domicilio')
    correo = fields.Char(string='Correo')
    representante = fields.Char(string='Representante')
    ciudad = fields.Char(string='Ciudad')
    telefono = fields.Char(string='Telefono')
    rfc = fields.Char(string='RFC')

    