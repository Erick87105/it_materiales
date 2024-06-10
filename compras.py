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
    
    fecha = fields.Datetime(string='Fecha y hora', default=fields.Datetime.now, readonly=True)

    proveedor_id = fields.Many2one('materiales.proveedor', string='Proveedor', required=True)
    status = fields.Selection(STATUS_SELECTION, string='Estado', default='creado')
    detalle_ids = fields.One2many('materiales.compras_detalle', 'compra_id', string='Detalles de Compra')
    
    total = fields.Float(string='Total estimado', compute='_compute_costo_estimado', store=True)

    @api.depends('detalle_ids.costo_estimado', 'detalle_ids.cantidad')
    def _compute_costo_estimado(self):
        for compra in self:
            total = sum(detalle.costo_estimado * detalle.cantidad for detalle in compra.detalle_ids)
            compra.total = total
            
    totalr = fields.Float(string='Total real', compute='_compute_total', store=True)

    @api.depends('detalle_ids.costo_real', 'detalle_ids.cantidad')
    def _compute_total(self):
        for compra in self:
            totalr = sum(detalle.costo_real * detalle.cantidad for detalle in compra.detalle_ids)
            compra.totalr = totalr
            
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
            
    @api.model
    def create(self,vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('Foliocompras')
        return super(Compras,self).create(vals)
    


class Detalle(models.Model):
    _name = 'materiales.compras_detalle'

    compra_id = fields.Many2one('materiales.comprados', string='Compra')
    requisicion_id = fields.Many2one('itsa.planeacion.requisiciones', string='Requisicion', required=True)
    producto = fields.Char(string='Producto')
    cantidad = fields.Integer(string='Cantidad', default=1)
    costo_estimado = fields.Float(string='Costo Estimado')
    costo_real = fields.Float(string='Costo Real')
    factura = fields.Char(string='Factura')
    
    @api.onchange('requisicion_id')
    def _onchange_requisicion_id(self):
        if self.requisicion_id:
            detalles = self.requisicion_id.req_ids
            if detalles:
                # Actualizar automáticamente los campos producto, cantidad y costo_estimado basándose en la requisición seleccionada
                self.update({
                    'producto': detalles[0].producto_id if detalles else '',
                    'cantidad': detalles[0].cantidad if detalles else 1,
                    'costo_estimado': detalles[0].costo if detalles else 0.0,
                })
                
                # Crear las líneas de detalles en compra_id basándose en los detalles de requisicion_id
                lineas = []
                for detalle in detalles:
                    lineas.append((0, 0, {
                        'producto': detalle.producto_id if detalle.producto_id else '',
                        'cantidad': detalle.cantidad,
                        'costo_estimado': detalle.costo,
                    }))
                self.compra_id.detalle_ids = lineas
            else:
                self.update({
                    'producto': '',
                    'cantidad': 1,
                    'costo_estimado': 0.0,
                })
                self.compra_id.detalle_ids = [(5, 0, 0)]  # Limpiar las líneas de detalles si no hay detalles en la requisición