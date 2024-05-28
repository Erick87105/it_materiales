from openerp import models, fields

class materiales(models.Model):
    _name = 'materiales.ubicaciones'
    
    Clave = fields.Char(string='Clave')
    Departamento = fields.Char(string='Departamento')
    Edificio = fields.Char(string='Edificio')
    Area = fields.Char(string='Area')
    