# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrderInheriting(models.Model):
    _inherit = 'sale.order'
    _rec_name = 'comfired_user_id'

    #[inheritance] : Adding New Field
    name = fields.Char('Inherited field name')

    # or we can id it using xpath [inheritance] : Adding New Field 
    comfired_user_id = fields.Many2one('res.users', string='Confirmed user')
    
    product_id = fields.Many2one('product.template', string='Product')

    def button_action(self):
        return

class ResPratnerInheriting(models.Model):
    _inherit = 'res.partner'

    #[inheritance] : Addding selection field
    company_type = fields.Selection(selection_add=[('walk_in', 'Walk In')])

class OdooInheritance(models.Model):
    _name = 'odoo.inheritance'
    _description = 'Odoo Inheritance'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('executive_director', 'Executive Director'),
        ('approve', 'Approved'),
        ('cancel', 'Cancelled'),
    ], tracking=True, required=True, copy=False, default='draft')

    def set_as_draft(self):
        for rec in self:
            rec.state = 'draft'
    
    def director_approver(self):
        for rec in self:
            rec.state = 'executive_director'

    def final_approver(self):
        for rec in self:
            rec.state = 'approve'

    def cancel(self):
        for rec in self:
            rec.state = 'cancel' 
   