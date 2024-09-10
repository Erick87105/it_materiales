# -*- coding: utf-8 -*-
from openerp import models, fields, api

class Departamentos(models.Model):
    _inherit = 'itsa.base.deptos'

class itsa_rh_empleados(models.Model):
    _inherit = 'itsa.rh.empleados'

class Entregaproductos(models.Model):
    _name = 'materiales.entregaproductos'
    
    STATUS_SELECTION = [
        ('creado', 'Creado'),
        ('aplicado', 'Aplicado'),
        ('cancelado', 'Cancelado'),
    ]
    status = fields.Selection(STATUS_SELECTION, string='Estado', default='creado')  # Estado de la entrega
    name = fields.Char(string='Folio', readonly=True)
    compra_id = fields.Many2one('materiales.comprados', string='Compra',domain="[('status', '=', 'recibido')]", required=True )
    responsable = fields.Char(string='Responsable de resguardo', compute='_compute_responsable', store=True)    
    fecha = fields.Datetime(string='Fecha y hora', default=fields.Datetime.now, readonly=True)
    departamento_id = fields.Many2one('itsa.base.deptos', string='Departamento de asignacion')
    ubicacion = fields.Char(string='Ubicación origen', default='Bodega materiales')
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
            self.responsable = self.departamento_id.jefe.name
        else:
            self.responsable = ''
            
    @api.depends('departamento_id')
    def _compute_responsable(self):
        for record in self:
            if record.departamento_id:
                jefe_name = record.departamento_id.jefe.name
                # Actualizamos el valor de responsable sin disparar el write
                record.update({'responsable': jefe_name})
            else:
                record.update({'responsable': ''})

    @api.multi
    def write(self, vals):
        # Evitar que se compute el responsable al escribir si ya está presente en los valores
        if 'responsable' not in vals:
            self._compute_responsable()
        return super(Entregaproductos, self).write(vals)

    
    @api.model
    def create(self, vals):
        record = super(Entregaproductos, self).create(vals)
        record._compute_responsable()
        return record

    # @api.multi
    # def write(self, vals):
    #     result = super(Entregaproductos, self).write(vals)
    #     self._compute_responsable()
    #     return result
            
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
    
    @api.onchange('ubicacion_id')
    def _onchange_ubicacion_id(self):
        if self.ubicacion_id:
            self.ubicacion_destino = self.ubicacion_id.Departamento
            self.edificio = self.ubicacion_id.Edificio
            self.area = self.ubicacion_id.Area
        else:
            self.ubicacion_destino = ''
            self.edificio = ''
            self.area = ''
    
    @api.model
    def _get_rango_cantidad(self):
        # Este método genera una lista de tuplas con números del 1 al 20
        return [(str(num), str(num)) for num in range(1, 500)]
    