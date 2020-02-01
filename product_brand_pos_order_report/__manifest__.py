# -*- coding: utf-8 -*-
# Copyright 2018 Tecnativa - David Vidal
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Product Brand in Point of Sale Orders Statistics',
    'version': '11.0.0.0.0',
    'category': 'Product',
    'author': 'Tecnativa,'
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/sale-reporting',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'product_brand',
    ],
    'data': [
        'reports/sale_report_view.xml',
    ],
    'installable': True,
}
