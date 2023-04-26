from odoo import api, fields, models, _ 

class WizardPractice(models.TransientModel):
    _name = 'wizard.practice'
    
    name = fields.Char(string='Name')
    product_id = fields.Many2one('product.template', string='Product')