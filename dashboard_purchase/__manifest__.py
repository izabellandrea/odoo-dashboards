# -*- coding: utf-8 -*-
{
	'name': "Dashboard for Purchase",

	'summary': """
			Dashboard for Purchase""",

	'author': "",
	
	'category': 'Uncategorized',
	'version': '15.0.1.0.0.I20240326',
	'license': "",
	'depends': ['board','purchase'],
	# always loaded
	'data': [
        'views/purchase.xml',
        'views/purchase_dashboard.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'dashboard_purchase/static/src/js/**/*',
        ],
    },
	'installable': True,
	'auto_install': False,
	'application': False,
}