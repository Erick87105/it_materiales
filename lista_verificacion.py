# -*- coding: utf-8 -*-
from openerp import models, fields, api
import re

class ListaVerificacion(models.Model):
    _name = 'lista.verificacion'
    _description = 'Lista de Verificación'

    name = fields.Char(string='Folio', readonly=True)
    area_verificacion = fields.Many2one('area.verificacion', string='Área en la que se realiza la verificación', required=True)
    jefe_area = fields.Many2one('res.users', string='Jefe/a del área en la que se realiza la verificación', required=True)
    trabajador_area = fields.Many2one('res.users', string='Trabajador/a del área', required=True)
    jefe_area_verificada = fields.Many2one('res.users', string='Jefe/a del área verificada', required=True)
    fecha = fields.Date(string='Fecha', default=fields.Date.context_today, required=True)
    detalle_ids = fields.One2many('lista.verificacion.detalle', 'lista_id', string='Verificación de infraestructura y equipo')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('Foliolistaverificacion')
        return super(ListaVerificacion, self).create(vals)

    def _sanitize_field(self, value):
        # Remover caracteres no válidos
        value = re.sub(r'[^\x20-\x7E]+', '', value)
        return value
    
    # Campo para los estados
    state = fields.Selection([
        ('creado', 'Creado'),
        ('verificado', 'Verificado'),
        ('aplicado', 'Aplicado')
    ], string='Estado', default='creado')

    @api.multi
    def action_verificar(self):
        """Método para cambiar el estado a 'Verificado'"""
        self.state = 'verificado'

    @api.multi
    def action_aplicar(self):
        """Método para cambiar el estado a 'Aplicado'"""
        self.state = 'aplicado'

class ListaVerificacionDetalle(models.Model):
    _name = 'lista.verificacion.detalle'
    _description = 'Detalle de la Verificación'

    lista_id = fields.Many2one('lista.verificacion', string='Lista de Verificación', ondelete='cascade', required=True)
    elemento_revisado = fields.Many2one('elemento.revisado', string='Elemento Revisado', required=True)
    hallazgo = fields.Text(string='Hallazgo')
    atendido = fields.Selection([('si', 'Sí'), ('no', 'No')], string='Atendido Inmediatamente', required=True)

class AreaVerificacion(models.Model):
    _name = 'area.verificacion'
    _description = 'Área de Verificación'

    name = fields.Char(string='Nombre', required=True)

class ElementoRevisado(models.Model):
    _name = 'elemento.revisado'
    _description = 'Elemento Revisado'

    name = fields.Char(string='Nombre', required=True)
