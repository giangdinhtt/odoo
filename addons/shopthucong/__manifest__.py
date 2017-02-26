# -*- coding: utf-8 -*-

{
    'name': 'shopthucong.com',
    'version': '0.1',
    'category': 'Point Of Sale',
    'sequence': 20,
    'summary': 'Point Of Sale modifications for shopthucong.com',
    'description': """
Main Features
-------------
* Beautify receipt billing
    """,
    'depends': ['point_of_sale','product'],
    'data': [
        'views/shopthucong_template.xml',
        'views/shopthucong.xml',
        'views/product_view.xml',
        'wizard/product_update_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'qweb': ['static/src/xml/pos.xml'],
    'website': 'http://www.shopthucong.com',
}
