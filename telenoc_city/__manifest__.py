# -*- coding: utf-8 -*-
{
    'name': "telenoc_city",

    'summary': """
        Add by default Country and City when Customer is created""",

    'description': """
        Add by default Country and City when Customer is created
        1.Riyadh
        2.Saudi Arabia
    """,

    'author': "Telenoc",
    'website': "https:www.telenoc.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}