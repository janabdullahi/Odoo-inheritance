from odoo import http
from odoo.http import request
import datetime

class ValidateRequestToDashboard(http.Controller):
    @http.route('/validate-dashboard-request', auth='user')
    def validate_dashboard_request(self): 
        # if  request.env.user.has_group('nl_dashboard.group_dashboard_inheritance'):
        return request.redirect(f'/dashboard/inheritance')
        # else:
            # request.not_found()
    
    def search_records(self, filterby, date_field, from_date=None, to_date=None, past_date=None):
        if filterby == 'custom_date' or filterby == 'yesterday' or filterby == 'today': 
            date_search = f"{date_field} BETWEEN '{from_date}' AND '{to_date}'"
        elif filterby == 'all':
            date_search = f"'' BETWEEN '' AND ''"
        else:
            date_search = ''
        return date_search
    
    def get_filterby(self, filterby, from_date, to_date):
        if filterby == 'all':
            return 'All'
        elif filterby == 'today':
            return 'Today'
        elif filterby == 'custom_date':
            return f'{from_date} To {to_date}'
        else:
            return f'{filterby.title().replace("_", " ")}'

    def set_from_date(self, filterby, from_date=None):
        if filterby == 'custom_date':
            return from_date
        if filterby == 'today':
            today = datetime.date.today() 
            return today.strftime('%Y-%m-%d')
        elif filterby == 'yesterday':
            yesterday = datetime.date.today() - datetime.timedelta(days=1)
            return yesterday.strftime('%Y-%m-%d')
        else:
            return ''

    def set_to_date(self, filterby, to_date=None):
        if filterby == 'custom_date':
            return to_date
        if filterby == 'today':
            today = datetime.date.today() 
            return today.strftime('%Y-%m-%d')
        elif filterby == 'yesterday':
            yesterday = datetime.date.today() - datetime.timedelta(days=1)
            return yesterday.strftime('%Y-%m-%d')
        else:
            return ''
    
   
    @http.route('/dashboard/inheritance', auth='user', website=True)
    def show_dashboard_inheritance(self, filterby='all', from_date=None, to_date=None):

        from_date = self.set_from_date(filterby, from_date)
        to_date = self.set_to_date(filterby, to_date)

        values = {
            'filterby': self.get_filterby(filterby, from_date, to_date),
            'total_executive_director': self._total_executive_director(filterby, from_date, to_date),
            'page_name': 'inheritance',
        }
        return request.render("nl_dashboard.odoo_inheritance_dashboard", values)
    
    def _total_executive_director(self, filterby, from_date, to_date):
        request.env.cr.execute(f'''
        SELECT
            COUNT(employee_id) 
        FROM 
            odoo_inheritance 
        WHERE 
            STATE = 'executive_director'
        AND
            {self.search_records(filterby, 'create_date::DATE', from_date, to_date)} 
        ''')
        return request.env.cr.fetchall()[0][0]