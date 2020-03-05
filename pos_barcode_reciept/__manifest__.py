{
    'name': 'POS Barcode Reciept',
    'summary': """POS Receipt with Barcode """,
    'version': '13.0.1.0',
    'description': """POS Receipt with Barcode""",
    'category': 'Point of Sale',
    'depends': ['base', 'point_of_sale'],
    'data': [
    	'views/import.xml',
    	'views/pos_order.xml',
    ],
    'qweb': ['static/src/xml/posticket.xml'],
    'images': ['static/description/banner.png'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}

