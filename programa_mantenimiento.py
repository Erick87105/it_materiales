# -*- coding: utf-8 -*-
from openerp import models, fields

class ProgramaMantenimiento(models.Model):
    _name = 'programa.mantenimiento'
    _description = 'Programa de Mantenimiento'

    semestre = fields.Selection(
        [('1', 'Ene/Jun '), ('2', 'Ago/Dic')],
        string='Semestre',
        required=True
    )
    def get_years():
        year_list = []
        for i in range(2024, 2044):
            year_list.append((i, str(i)))
        return year_list

    ano = fields.Selection(selection=get_years(), string='Año', required=True)
    elaborado_por = fields.Many2one('res.users','Elaborado por', required=True)
    aprobado_por = fields.Many2one('res.users', string='Aprobado por', required=True)
    fecha_elaboracion= fields.Datetime(string='Fecha de Elaboración', default=fields.Datetime.now) 
    fecha_aprobacion = fields.Date(string='Fecha de Aprobación')
    mantenimiento_ids = fields.One2many('programa.mantenimiento.detalle', 'programa_id', string='Mantenimientos')

class ProgramaMantenimientoDetalle(models.Model):
    _name = 'programa.mantenimiento.detalle'
    _description = 'Detalle del Programa de Mantenimiento'

    programa_id = fields.Many2one('programa.mantenimiento', string='Programa', required=True, ondelete='cascade')
    service_number = fields.Integer(string='No.' , default=1 )

    
    servicio = fields.Text(string='Descripción del Servicio', required=True)
    tipo = fields.Selection(
        [('i', 'Interno'), ('e', 'Externo'),],
        string='Tipo',
        required=True
    )
    status = fields.Selection(
        [('r', 'R'), ('p', 'P'), ('o', 'O')],
        string='MTTO',
        required=True
    )
    ene = fields.Boolean(string='EN')
    feb = fields.Boolean(string='FB')
    mar = fields.Boolean(string='MA')
    abr = fields.Boolean(string='AB')
    may = fields.Boolean(string='MY')
    jun = fields.Boolean(string='JN')
    jul = fields.Boolean(string='JL')
    ago = fields.Boolean(string='AG')
    sep = fields.Boolean(string='SE')
    oct = fields.Boolean(string='OC')
    nov = fields.Boolean(string='NO')
    dic = fields.Boolean(string='DI')
    
    status = fields.Selection(
        [('r', 'R'), ('p', 'P'), ('o', 'O')],
        string='MTTO',
        required=True
    )
