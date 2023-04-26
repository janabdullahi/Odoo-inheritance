# -*- coding: utf-8 -*-
{
    'name': "Odoo Inheritance",

    'summary': """
        Odoo Inheritance""",

    'description': """
        Odoo Inheritance
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'sale'],

    'data': [
        'security/ir.model.access.csv',
        'wizards/wizard_view.xml',
        'views/views.xml',
        'reports/sale_report_inherit.xml',
    ],
    
}
