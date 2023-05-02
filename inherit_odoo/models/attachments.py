from odoo import models, fields, api, _
from datetime import date, datetime


class Attachment(models.Model):
    _name = 'attachment.attachment'
    _description = 'File Attachment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    name = fields.Char(string='Document Name', required=True)
    date = fields.Date(default=datetime.today())
    document_file = fields.Binary(string=" ")
    active = fields.Boolean(default=True)
    employee_id = fields.Many2one('odoo.inheritance')