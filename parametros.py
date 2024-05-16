# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.exceptions import ValidationError

class MaterialesParametros(models.Model):
    _name = 'materiales.parametros'
    
    key = fields.Char('Clave', required=True, index=True)
    value = fields.Char('Valor', required=True)
