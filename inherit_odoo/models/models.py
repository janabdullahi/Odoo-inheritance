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
    invoice_id = fields.Many2one(comodel_name='account.move', copy=False)
    invoice_count  = fields.Integer(compute='_count_invoice')
    attachments_count = fields.Integer(compute='compute_attachments_count')

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

    def action_create_invoice(self):
            for rec in self:
                if rec.state != 'approve':
                    raise UserError(f'You Cannot create invoice in this {rec.state} state.')
                
                if  rec.invoice_id:  
                    raise UserError('Invoice already created') 

                invoice_lines = [{
                        'name': line.product_id.name,
                        'product_id': line.product_id.id,
                        'price_subtotal': line.price_subtotal
                        } for line in rec.product_line_ids]

                invoice_vals = {
                    'partner_id':  rec.employee_id.id,
                    'move_type': 'out_invoice',
                    'invoice_line_ids': invoice_lines
                }

                invoice = rec.env['account.move'].sudo().create(invoice_vals)
                rec.invoice_id = invoice.id
                return rec.action_view_invoice()

    @api.depends('invoice_id')
    def _count_invoice(self):
        for rec in self:
            rec.invoice_count = len(rec.invoice_id)
    
    def action_view_invoice(self):
        for rec in self:
            if rec.invoice_id:
                return {
                    'name': 'Invoice',
                    'view_mode': 'form',
                    'res_model': 'account.move',
                    'context': "{'move_type': 'out_invoice'}",
                    'type': 'ir.actions.act_window',
                    'res_id': rec.invoice_id.id,
                }

    def compute_attachments_count(self):
        for rec in self:
            rec.attachments_count = self.env['attachment.attachment'].search_count([('employee_id','=', self.id)])

    def attachments_view_result(self): 
        for request in self:
            return {
                'name': 'Document Type',
                'view_mode': 'tree,form',
                'res_model': 'attachment.attachment',   
                'type': 'ir.actions.act_window',
                'domain': [('employee_id', '=', self.id)],   
                'context': {'default_employee_id': self.id},
            }
   