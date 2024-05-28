# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Entregaproductos(models.Model):
    _name = 'materiales.entregaproductos'
    
    STATUS_SELECTION = [
        ('creado', 'Creado'),
        ('aplicado', 'Aplicado'),
        ('cancelado', 'Cancelado'),
    ]
    
    name = fields.Char(string='Folio', readonly=True)  
    fecha = fields.Date(string='Fecha', default=fields.Date.context_today, readonly=True)  # Fecha de entrega
    status = fields.Selection(STATUS_SELECTION, string='Estatus', default='creado')  # Estado de la entrega
    compra_id = fields.Many2one('materiales.comprados', string='Compra', required=True)

    responsable = fields.char(string='Responsable de resguardo')  
    departamento_entregaproductos = fields.Selection(
    [('administracion', 'Administración'),
     ('contabilidad', 'Contabilidad'),
     ('recursos_humanos', 'Recursos Humanos'),
     ('mantenimiento', 'Mantenimiento'),
     ('servicios_escolares', 'Servicios Escolares'),
     ('otros', 'Otros')],
    string='Departamento a asignar',
    required=True,
    )


    detalle_ids = fields.One2many('materiales.detalleentrega', 'entregaproductos_id', string='Detalles de Entrega')  # Detalles de la entrega
    @api.model
    def create(self, vals):
        # Generar un folio único para la recepción al crearla
        vals['name'] = self.env['ir.sequence'].next_by_code('Folioentregaproductos')
        return super(entregaproductos, self).create(vals)
    
    @api.multi
    def action_aplicar(self):
        # Cambiar el estado de la recepción a 'aplicado'
        self.write({'status': 'aplicado'})
        for detalle in self.detalle_ids:
            # Cambiar el estado de la compra asociada a 'recibido'
            detalle.compra_id.action_receive()
    
    @api.multi
    def action_cancelar(self):
        # Cambiar el estado de la recepción a 'cancelado'
        self.write({'status': 'cancelado'})

class Detalleentrega(models.Model):
    _name = 'materiales.detalleentrega'

    entregaproductos_id = fields.Many2one('materiales.entregaproductos', string='Entrega')  # Relación con la recepción
      # Relación con la compra
    producto = fields.Char(string='Producto')  # Producto recibido
    cantidad = fields.Integer(string='Cantidad')  # Cantidad recibida
    
    costo_real = fields.Float(string='Costo Real')  # Costo real del producto

    @api.onchange('compra_id')
    def _onchange_compra_id(self):
        if self.compra_id:
            detalles = self.compra_id.detalle_ids
            # Actualizar automáticamente los campos producto, cantidad y costo_real basándose en la compra seleccionada
            self.update({
                'producto': detalles[0].producto if detalles else '',
                'cantidad': detalles[0].cantidad if detalles else 1,
                'costo_real': detalles[0].costo_real if detalles else 0.0,
            })
