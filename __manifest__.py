# -*- coding: utf-8 -*-

{
    'name': 'Doctor Training',
    'version': '1.0',
    'category': 'Doctor',
    'author': 'Mert Ç.',
    'sequence': -100,
    'summary': """Doctor Management Mert Ç.""",
    'description': "",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/doctor_view.xml',
        'views/department_view.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml',
        'views/treatment_view.xml',
        'views/wizard_view.xml',
    ],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
