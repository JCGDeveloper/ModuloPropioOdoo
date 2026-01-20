# -*- coding: utf-8 -*-
{
    'name': "HR Employee Extension (DNI/NSS)",
    'summary': """Extensión de empleados con DNI y NSS español""",
    'description': """
        Módulo para añadir campos de identificación española:
        - DNI (con validación)
        - Número de la Seguridad Social (con validación)
    """,
    'author': "Alumno 2DAM",
    'category': 'Human Resources',
    'version': '0.1',
    'depends': ['base', 'hr'],
    'data': [
        'views/hr_employee_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
