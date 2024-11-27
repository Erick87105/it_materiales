# -*- coding: utf-8 -*-
from openerp import models, fields, api

class TrabajadoresMateriales(models.Model):
    _name = 'trabajadores.materiales'
    _description = 'Registro de Trabajadores de Materiales'

    name = fields.Char(string='Nombre', required=True)
    employee_id = fields.Char(string='ID del Empleado', required=True)
    department = fields.Char(string='Departamento', default='RECURSOS MATERIALES Y SERVICIOS')
    position = fields.Char(string='Puesto')
    date_hired = fields.Date(string='Fecha de Contratación')
    active = fields.Boolean(string='Activo', default=True)
