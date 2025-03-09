# -*- coding: utf-8 -*-
{
	'name': "Dashboard for Account ",

	'summary': """
			Dashboard for Account""",

	'author': "",
	
	'category': 'Uncategorized',
	'version': '15.0.1.0.0.I20240326',
	'license': "",
	'depends': ['board','account'],
	# always loaded
	'data': [
        'views/account.xml',
        'views/account_dashboard.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'dashboard_account/static/src/js/**/*',
        ],
    },
	'installable': True,
	'auto_install': False,
	'application': False,
}