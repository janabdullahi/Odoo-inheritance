# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class inherit_odoo(models.Model):
#     _name = 'inherit_odoo.inherit_odoo'
#     _description = 'inherit_odoo.inherit_odoo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
