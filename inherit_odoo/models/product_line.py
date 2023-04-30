# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class PrescriptionOrderLine(models.Model):
    _name = 'product.line'
    _description = 'Product Line'

    product_id = fields.Many2one('product.product', string='Product', required=True)
    product_line_id = fields.Many2one('odoo.inheritance', string='Order Reference', ondelete='cascade', index=True)
    description = fields.Text(string='Description')
    units = fields.Float(default=0.0)
    available_quantity = fields.Float()
    list_price = fields.Float(related='product_id.list_price')
    currency_id = fields.Many2one(comodel_name='res.currency', string='Currency', related='product_id.currency_id')
    price_subtotal = fields.Monetary(compute='_compute_amount', string='Subtotal')

    @api.depends('units', 'list_price')
    def _compute_amount(self):
        for line in self:
            line.price_subtotal = line.units * line.list_price