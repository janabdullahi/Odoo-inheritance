# -*- coding: utf-8 -*-
{
    'name': 
        " Odoo Inheritance, Wizard and more practice",

    'summary':
         """
            Odoo Inheritance, Wizard and more practice
        """,

    'description': """
        Odoo Inheritance
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'sale', 'hr', 'nl_dashboard'],

    'data': [
        'security/ir.model.access.csv',
        'wizards/wizard_view.xml',
        'views/views.xml',
        'views/attachments.xml',
        'data/sequence.xml',
        'reports/sale_report_inherit.xml',
    ],
    
}
