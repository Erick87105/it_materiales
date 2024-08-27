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
    
    tipo_mantenimiento_i_e = fields.Selection([
        ('interno', 'Interno'),
        ('externo', 'Externo')
    ], string='Tipo de mantenimiento (I/E)', required=True)
    
    tipo_mantenimiento_p_c = fields.Selection([
        ('preventivo', 'Preventivo'),
        ('correctivo', 'Correctivo'),
    ], string='Tipo de mantenimiento (P/C)', required=True)
    
    tipo_servicio = fields.Selection([
        ('herreria', 'Herrería'),
        ('electricidad', 'Electricidad'),
        ('plomeria', 'Plomería'),
        ('pintura', 'Pintura'),
        ('obra_civil', 'Obra Civil'),
    ], string='Tipo de servicio', required=True)
    
    asignado_a = fields.Many2one('res.users', string='Asignado a', required=True)
    fecha_realizacion = fields.Date(string='Fecha de realización')
    
    e_p_p_ids = fields.Many2one('materiales.orden.equipo.proteccion', string='Equipo de protección personal')
    
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
    
    personal_protection_equipment = fields.Many2many('personal.protection.equipment', string='Equipo de protección personal')

class PersonalProtectionEquipment(models.Model):
    _name = 'personal.protection.equipment'
    
    name = fields.Char('Nombre del equipo', required=True)
