# -*- coding: utf-8 -*-
{
    'name': 'Medical Shop',
    'category': 'eCommerce',
    'summary': 'Medical Shop',
    'website': '',
    'version': '1.0',
    'author': 'Kanak Info Systems',
    'description': """
Medical Shop
============
    """,
    'depends': ['website_sale'],
    'data': [
        'data/data.xml',
        'views/shop_views.xml',
        'views/assets_templates.xml',
        'views/shop_templates.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
