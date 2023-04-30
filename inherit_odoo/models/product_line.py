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
