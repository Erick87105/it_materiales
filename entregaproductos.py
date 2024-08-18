# -*- coding: utf-8 -*-
from openerp import models, fields, api

class Entregaproductos(models.Model):
    _name = 'materiales.entregaproductos'
    
    STATUS_SELECTION = [
        ('creado', 'Creado'),
        ('aplicado', 'Aplicado'),
        ('cancelado', 'Cancelado'),
    ]
    status = fields.Selection(STATUS_SELECTION, string='Estado', default='creado')  # Estado de la entrega
    name = fields.Char(string='Folio', readonly=True)
    compra_id = fields.Many2one('materiales.comprados', string='Compra', required=True )
    responsable = fields.Char(string='Responsable de resguardo')
    fecha = fields.Datetime(string='Fecha y hora', default=fields.Datetime.now, readonly=True)
    departamento_id = fields.Many2one('materiales.departamento', string='Departamento de asignacion')
    ubicacion = fields.Char(string='Ubicación', default='Bodega materiales', readonly=True)
    detalle_ids = fields.One2many('materiales.detalleentrega', 'entregaproductos_id', string='Detalle recepción')
    
    @api.multi
    def action_aplicar(self):
        # Cambiar el estado de la entrega a 'aplicado'
        self.write({'status': 'aplicado'})
    
    @api.multi
    def action_cancelar(self):
        # Cambiar el estado de la entrega a 'cancelado'
        self.write({'status': 'cancelado'})

    @api.onchange('departamento_id')
    def _onchange_departamento_id(self):
        if self.departamento_id:
            self.responsable = self.departamento_id.titular
        else:
            self.responsable = ''

    @api.model
    def create(self, vals):
        if 'departamento_id' in vals:
            departamento = self.env['materiales.departamento'].browse(vals['departamento_id'])
            vals['responsable'] = departamento.titular if departamento else ''
        return super(Entregaproductos, self).create(vals)

    @api.multi
    def write(self, vals):
        if 'departamento_id' in vals:
            departamento = self.env['materiales.departamento'].browse(vals['departamento_id'])
            vals['responsable'] = departamento.titular if departamento else ''
        return super(Entregaproductos, self).write(vals)
            
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('Folioentregaproductos')
        return super(Entregaproductos, self).create(vals)

    @api.multi
    def action_aplicar(self):
        self.write({'status': 'aplicado'})

class Detalleentrega(models.Model):
    _name = 'materiales.detalleentrega'

    entregaproductos_id = fields.Many2one('materiales.entregaproductos', string='Entrega')
    producto_id = fields.Many2one('materiales.productos', string='Producto')
    #cantidad = fields.Integer(string='Cantidad')
    requisicion_id = fields.Many2one('itsa.planeacion.requisiciones', string='Referencia línea de requisición', required=True)
    ubicacion_id = fields.Many2one("materiales.ubicaciones",string='Clave ubicacion destino')
    
    ubicacion_destino = fields.Char(string='Ubicación destino')
    edificio = fields.Char(string='Edificio')
    area = fields.Char(string='Área')
    cantidad = fields.Selection(selection='_get_rango_cantidad', string='Cantidad')

    @api.model
    def _get_rango_cantidad(self):
        # Este método genera una lista de tuplas con números del 1 al 20
        return [(str(num), str(num)) for num in range(1, 500)]
    