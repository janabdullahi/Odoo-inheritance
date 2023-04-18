# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrderInheriting(models.Model):
    _inherit = 'sale.order'

    #[inheritance] : Adding New Field
    name = fields.Char('Inherited field name')

class ResPratnerInheriting(models.Model):
    _inherit = 'res.partner'

    #[inheritance] : Addding selection field
    company_type = fields.Selection(selection_add=[('walk_in', 'Walk In')])
