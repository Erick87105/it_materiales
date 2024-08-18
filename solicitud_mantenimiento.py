# -*- coding: utf-8 -*-

from openerp import models, fields, api

class SolicitudMantenimiento(models.Model):
    _name = 'solicitud.mantenimiento'
    _description = 'Solicitud de Mantenimiento Correctivo'

    STATUS_SELECTION = [
        ('creado', 'Creado'),
        ('recibido', 'Recibido'),
        ('cancelado', 'Cancelado'),
    ]

    name = fields.Char(string='Folio', readonly=True)
    tipo_mantenimiento = fields.Many2one('tipo.mantenimiento', string='Tipo de mantenimiento', required=True)
    area_solicitante = fields.Many2one('area.solicitante', string='Área solicitante', required=True)
    fecha_solicitud = fields.Date(string='Fecha de solicitud', default=fields.Date.context_today, readonly=True)
     
    nombre_solicitante = fields.Many2one('res.users', string='Nombre del solicitante', required=True)
    descripcion = fields.Text()
    status = fields.Selection(STATUS_SELECTION, string='Estado', default='creado')


    @api.model
    def create(self,vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('Foliosolicitud')
        return super(SolicitudMantenimiento,self).create(vals)

class TipoMantenimiento(models.Model):
    _name = 'tipo.mantenimiento'
    _description = 'Tipo de Mantenimiento'

    name = fields.Char(string='Nombre', required=True)

class AreaSolicitante(models.Model):
    _name = 'area.solicitante'
    _description = 'Área Solicitante'

    name = fields.Char(string='Nombre', required=True)
