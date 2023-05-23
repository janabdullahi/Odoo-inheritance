from odoo import http
from odoo.http import request

class controller(http.Controller):
    @http.route('/admin', type='http', auht='user')
    def index(self):
        return request.render('inherit_odoo.admin')