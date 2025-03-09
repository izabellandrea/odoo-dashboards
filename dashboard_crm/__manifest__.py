# -*- coding: utf-8 -*-
{
	'name': "Dashboard for CRM",

	'summary': """
			Dashboard for CRM""",

	'author': "",
	
	'category': 'Uncategorized',
	'version': '15.0.1.0.0.I20240326',
	'license': "",
	'depends': ['board','crm'],
	# always loaded
	'data': [
        'views/crm.xml',
        'views/crm_dashboard.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'dashboard_crm/static/src/js/**/*',
        ],
    },
	'installable': True,
	'auto_install': False,
	'application': False,
}