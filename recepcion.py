# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Recepcion(models.Model):
    _name = 'materiales.recepcion'
    
    STATUS_SELECTION = [
        ('creado', 'Creado'),
        ('aplicado', 'Aplicado'),
        ('cancelado', 'Cancelado'),
    ]
    
    name = fields.Char(string='Folio', readonly=True)  # Folio de recepción
    #fecha = fields.Date(string='Fecha', default=fields.Date.context_today, readonly=True)  # Fecha de recepción
    fecha = fields.Datetime(string='Fecha y hora', default=fields.Datetime.now, readonly=True)
    status = fields.Selection(STATUS_SELECTION, string='Estado', default='creado')  # Estado de la recepción
    observaciones = fields.Text(string='Observaciones')  # Observaciones de la recepción
    ubicacion_recepcion = fields.Selection(
        [('bodega', 'Bodega Materiales'), ('otros', 'Otros')],
        string='Ubicación de Recepción', required=True, default='bodega'
    )  # Ubicación de la recepción
    detalle_ids = fields.One2many('materiales.detallerec', 'recepcion_id', string='Detalles de Recepción')  # Detalles de la recepción

    @api.model
    def create(self, vals):
        # Generar un folio único para la recepción al crearla
        vals['name'] = self.env['ir.sequence'].next_by_code('Foliorecepciones')
        return super(Recepcion, self).create(vals)
    
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

class Detallerec(models.Model):
    _name = 'materiales.detallerec'

    recepcion_id = fields.Many2one('materiales.recepcion', string='Recepción')  # Relación con la recepción
    compra_id = fields.Many2one('materiales.comprados', string='Compra', required=True)  # Relación con la compra
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
