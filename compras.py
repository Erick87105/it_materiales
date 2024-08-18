# -*- coding: utf-8 -*-
from openerp import models, fields, api

class Requisiciones(models.Model):
    _inherit = 'itsa.planeacion.requisiciones'

class RequisicionesDet(models.Model):
    _inherit = 'itsa.planeacion.requisiciones_det'


class Compras(models.Model):
    _name = 'materiales.comprados'

    STATUS_SELECTION = [
        ('creado', 'Creado'),
        ('pedido', 'Pedido'),
        ('recibido', 'Recibido'),
        ('cancelado', 'Cancelado'),
    ]

    name = fields.Char(string='Folio', readonly=True)
    fecha = fields.Datetime(string='Fecha y hora', default=fields.Datetime.now, readonly=True)
    proveedor_id = fields.Many2one('materiales.proveedor', string='Proveedor', required=True)
    requisicion_ids = fields.Many2many('itsa.planeacion.requisiciones', string='Requisiciones')
    status = fields.Selection(STATUS_SELECTION, string='Estado', default='creado')

    total = fields.Float(string='Total estimado', compute='_compute_costo_estimado', store=True)
    totalr = fields.Float(string='Total real', compute='_compute_total', store=True)

    compra_detalle_ids = fields.One2many('materiales.comprasdetalle', 'compra_id', string='Detalles de Compra')

    @api.depends('compra_detalle_ids.costo_estimado')
    def _compute_costo_estimado(self):
        for compra in self:
            total = sum(detalle.costo_estimado for detalle in compra.compra_detalle_ids)
            compra.total = total

    @api.depends('compra_detalle_ids.importe_real')
    def _compute_total(self):
        for compra in self:
            totalr = sum(detalle.importe_real for detalle in compra.compra_detalle_ids)
            compra.totalr = totalr

    @api.multi
    def action_confirm(self):
        self.write({'status': 'pedido'})

    @api.multi
    def action_receive(self):
        self.write({'status': 'recibido'})

    @api.multi
    def action_cancel(self):
        self.write({'status': 'cancelado'})

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('Foliocompras')
        compra = super(Compras, self).create(vals)
        compra.copy_requisiciones_to_detalle()
        return compra

    @api.multi
    def copy_requisiciones_to_detalle(self):
        self.ensure_one()
        detalle_existente = set()
        for detalle in self.compra_detalle_ids:
            detalle_existente.add((detalle.req_id.id, detalle.producto))

        detalles = []
        for requisicion in self.requisicion_ids:
            requisicion_detalles = self.env['itsa.planeacion.requisiciones_det'].search([('req_id', '=', requisicion.id)])
            for requisicion_det in requisicion_detalles:
                if (requisicion_det.req_id.id, requisicion_det.producto_id) not in detalle_existente:
                    detalle_vals = {
                        'compra_id': self.id,
                        'req_id': requisicion_det.req_id.id,
                        'producto': requisicion_det.producto_id,
                        'cantidad': requisicion_det.cantidad,
                        'costo_estimado': requisicion_det.costo,
                        'importe_real': requisicion_det.importe_real,
                    }
                    detalles.append((0, 0, detalle_vals))
        self.write({'compra_detalle_ids': detalles})

class ComprasDetalle(models.Model):
    _name = 'materiales.comprasdetalle'

    compra_id = fields.Many2one('materiales.comprados', string='Compra', required=True)
    req_id = fields.Many2one('itsa.planeacion.requisiciones', string='Ref. Req', readonly=True)
    producto = fields.Char(string='Producto', required=True, readonly=True)
    cantidad = fields.Integer(string='Cantidad', required=True, readonly=True)
    costo_estimado = fields.Float(string='Costo Estimado', required=True, readonly=True)
    importe_real = fields.Float(string='Costo real', readonly=True)
