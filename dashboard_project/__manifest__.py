# -*- coding: utf-8 -*-
{
	'name': "Dashboard for Project",

	'summary': """
			Dashboard for Project""",

	'author': "",
	
	'category': 'Uncategorized',
	'version': '15.0.1.0.0.I20240326',
	'license': "",
	'depends': ['board','project'],
	# always loaded
	'data': [
        'views/project.xml',
        'views/project_dashboard.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'dashboard_project/static/src/js/**/*',
        ],
    },
	'installable': True,
	'auto_install': False,
	'application': False,
}