# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

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
    'depends': ['account', 'point_of_sale'],
    'data': [
        'views/shopthucong_template.xml',
        'views/shopthucong.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'qweb': ['static/src/xml/pos.xml'],
    'website': 'http://www.shopthucong.com',
}
