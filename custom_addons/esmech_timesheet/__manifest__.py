# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Esmech Timesheet',
    'version': '1.0',
    'category': 'Services/Timesheets',
    'summary': 'Track employee time on tasks',
    'description': """
This module implements a timesheet system.
==========================================

Each employee can encode and track their time spent on the different projects.

Lots of reporting on time and employee tracking are provided.

    """,
    'website': 'https://www.odoo.com/page/timesheet-mobile-app',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/record_employees_inherit_views.xml',
        'views/punch_in_out_views.xml',

    ],
    'qweb': [

    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
