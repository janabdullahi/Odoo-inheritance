# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrderInheriting(models.Model):
    _inherit = 'sale.order'

    #[inheritance] : Adding New Field
    name = fields.Char('Inherited field name')
