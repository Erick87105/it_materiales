from openerp import models, fields

class Productos(models.Model):
    _name = 'materiales.productos'

    name = fields.Char('Nombre del Producto', required=True)
    brand = fields.Char('Marca')
    model = fields.Char('Modelo')
    type = fields.Selection([
        ('consumible', 'Consumible'),
        ('activo', 'Activo')
    ], 'Tipo de producto', required=True)
    value = fields.Float('Valor actual')
    status = fields.Float('Estatus', default=1.00)
    maintenance_program = fields.Boolean('Programa de mantenimiento')
    observations = fields.Text('Observaciones')
    odoo_id = fields.Char('Identificación de serie')
    years_of_life = fields.Integer('Años de vida util')
    description = fields.Text('Descripción')
