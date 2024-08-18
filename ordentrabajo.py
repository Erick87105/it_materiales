# -*- coding: utf-8 -*-

from openerp import models, fields, api

class MaterialesOrdenTrabajo(models.Model):
    _name = 'materiales.orden.trabajo'
    _description = 'Orden de Trabajo de Mantenimiento en Materiales'
    
    name = fields.Char(string='Folio', readonly=True)

    @api.model
    def create(self, vals):
        # Asignar un folio único utilizando una secuencia llamada 'materiales_orden_trabajo'
        vals['name'] = self.env['ir.sequence'].next_by_code('materiales_orden_trabajo')
        return super(MaterialesOrdenTrabajo, self).create(vals)
    
   # name = fields.Char(string='Folio', readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('materiales.orden.trabajo'))
    fecha = fields.Date(string='Fecha', required=True, default=fields.Date.context_today)
    
    tipo_mantenimiento = fields.Selection([
        ('interno', 'Interno'),
        ('externo', 'Externo')
    ], string='Tipo de mantenimiento a realizar', required=True)
    
    tipo_servicio = fields.Selection([
        ('preventivo', 'Preventivo'),
        ('correctivo', 'Correctivo'),
        ('herreria', 'Herrería'),
        ('electricidad', 'Electricidad'),
        ('plomeria', 'Plomería'),
        ('pintura', 'Pintura'),
        ('obra_civil', 'Obra Civil'),
    ], string='Tipo de servicio', required=True)
    
    asignado_a = fields.Many2one('res.users', string='Asignado a', required=True)
    fecha_realizacion = fields.Date(string='Fecha de realización')
    
    proteccionpersonal = fields.Many2many('materiales.equipo.proteccionp', string='Equipo de protección personal')
    
    residuos_generados = fields.Selection([
        ('rsu', 'RSU'),
        ('rp', 'Residuos Peligrosos'),
        ('rme', 'Residuos Reciclables'),
        ('otros', 'Otros')
    ], string='Residuos generados')
    
    disposicion_residuos = fields.Text(string='Disposición de Residuos')
    
    descripcion_trabajo = fields.Text(string='Descripción del trabajo realizado')
    materiales_utilizados = fields.Text(string='Materiales utilizados')
    
    verificado_por = fields.Many2one('res.users', string='Verificado y liberado por')
    fecha_liberacion = fields.Date(string='Fecha liberación')
    aprobado_por = fields.Many2one('res.users', string='Aprobado por')
    fecha_aprobacion = fields.Date(string='Fecha aprobación')

class MaterialesEquipoProteccion(models.Model):
    _name = 'materiales.equipo.proteccion.personal'
    _description = 'Equipo de Protección Personal en Materiales'

    nombre = fields.Char(string='Nombre', required=True)
