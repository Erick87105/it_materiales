# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Compras(models.Model):
    _name = 'materiales.comprados'

    STATUS_SELECTION = [
        ('creado', 'Creado'),
        ('pedido', 'Pedido'),
        ('recibido', 'Recibido'),
        ('cancelado', 'Cancelado'),
    ]

    name = fields.Char(string='Folio',readonly=True)
    fecha = fields.Date(string='Fecha', default=fields.Date.context_today, readonly=True)
    proveedor_id = fields.Many2one('materiales.proveedor', string='Proveedor', required=True)
    status = fields.Selection(STATUS_SELECTION, string='Estatus', default='creado')
    detalle_ids = fields.One2many('materiales.compras_detalle', 'compra_id', string='Detalles de Compra')
    
    total = fields.Float(string='Total', compute='_compute_total', store=True)

    @api.depends('detalle_ids.costo_estimado', 'detalle_ids.cantidad')
    def _compute_total(self):
        for compra in self:
            total = sum(detalle.costo_estimado * detalle.cantidad for detalle in compra.detalle_ids)
            compra.total = total
    # Método para cambiar el estado de 'Creado' a 'Pedido'
    @api.multi
    def action_confirm(self):
        self.write({'status': 'pedido'})

    # Método para cambiar el estado de 'Pedido' a 'Recibido'
    @api.multi
    def action_receive(self):
        self.write({'status': 'recibido'})

    # Método para cambiar el estado de 'Creado', 'Pedido' o 'Recibido' a 'Cancelado'
    @api.multi
    def action_cancel(self):
        self.write({'status': 'cancelado'})

    # def _compute_total(self):
    #     for compra in self:
    #         total = sum(detalle.costo_real for detalle in compra.detalle_ids)
    #         compra.total = total
            
    @api.model
    def create(self,vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('Foliocompras')
        return super(Compras,self).create(vals)
    
class Detalle(models.Model):
    _name = 'materiales.compras_detalle'

    compra_id = fields.Many2one('materiales.comprados', string='Compra')
    concepto_requisicion = fields.Selection([('concepto1', 'Concepto 1'), ('concepto2', 'Concepto 2'), ('concepto3', 'Concepto 3')], string='Concepto Requisición')
    producto = fields.Char(string='Producto')
    cantidad = fields.Integer(string='Cantidad', default=1)
    costo_estimado = fields.Float(string='Costo Estimado')
    costo_real = fields.Float(string='Costo Real')
    factura = fields.Char(string='Factura')
