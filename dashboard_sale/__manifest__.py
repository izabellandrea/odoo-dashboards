# -*- coding: utf-8 -*-
{
	'name': "Dashboard for Sale",

	'summary': """
			Dashboard for Sale""",

	'author': "",
	
	'category': 'Uncategorized',
	'version': '15.0.1.0.0.I20240326',
	'license': "",
	'depends': ['sale'],
	# always loaded
	'data': [
        'views/sale.xml',
        'views/sale_dashboard.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'dashboard_sale/static/src/js/**/*',
        ],
    },
	'installable': True,
	'auto_install': False,
	'application': False,
}