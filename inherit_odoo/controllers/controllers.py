# -*- coding: utf-8 -*-
# from odoo import http


# class InheritOdoo(http.Controller):
#     @http.route('/inherit_odoo/inherit_odoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inherit_odoo/inherit_odoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inherit_odoo.listing', {
#             'root': '/inherit_odoo/inherit_odoo',
#             'objects': http.request.env['inherit_odoo.inherit_odoo'].search([]),
#         })

#     @http.route('/inherit_odoo/inherit_odoo/objects/<model("inherit_odoo.inherit_odoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inherit_odoo.object', {
#             'object': obj
#         })
