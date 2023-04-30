# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import Warning, UserError, ValidationError

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
    _order = "employee_id desc" 
    _rec_name = 'employee_id'

    ref = fields.Char(string='Reference', default=lambda self: _('New'), copy=False)
    employee_id = fields.Many2one('hr.employee', string="Employee Name", required=True, readonly=True, states={'draft': [('readonly', False)]})
    last_name = fields.Char(string="Last Name", readonly=True, states={'draft': [('readonly', False)]})
    phone = fields.Char(readonly=True, states={'draft': [('readonly', False)]})
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True, default=lambda self: self.env.company)
    department_id = fields.Many2one('hr.department', string='Department', related='employee_id.department_id',store=True)
    active = fields.Boolean(default=True)
    product_line_ids = fields.One2many(comodel_name='product.line', inverse_name='product_line_id', copy=True, readonly=True, states={'draft': [('readonly', False)]})
    
    
    @api.model
    def create(self, values):
        values['ref'] = self.env['ir.sequence'].next_by_code('odoo.inheritance') or _('New')
        return super(OdooInheritance, self).create(values)

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
    
    def copy(self, default=None):
        for rec in self:
            if rec.state != 'draft':
                raise ValidationError(_('You cannot duplicate request unless it is in draft state.'))
            return super(OdooInheritance, self).copy(default=default)

    def unlink(self):
        for rec in self:
            if rec.state != 'draft':
                raise ValidationError(_('You cannot delete request unless it is in draft state.'))
            super(OdooInheritance, rec).unlink()
   