
from openerp import models, fields

class Proveedor(models.Model):
    _name = 'materiales.proveedor'

    name = fields.Char(string='Nombre de la Empresa', required=True)
    domicilio = fields.Char(string='Domicilio')
    correo = fields.Char(string='Correo')
    representante = fields.Char(string='Representante')
    ciudad = fields.Char(string='Ciudad')
    telefono = fields.Char(string='Telefono')
    rfc = fields.Char(string='RFC')
    