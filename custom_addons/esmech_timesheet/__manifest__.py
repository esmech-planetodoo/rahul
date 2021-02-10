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
        'views/menu_items_views.xml',
        'views/organization_views.xml',
        'views/employee_job_views.xml',
        'views/employee_info_data_views.xml',
        'views/hr_employee_master_views.xml',
        'views/employee_leaveinfo_views.xml',
        'views/employee_project_views.xml',
        'views/employee_timesheet_views.xml',
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
