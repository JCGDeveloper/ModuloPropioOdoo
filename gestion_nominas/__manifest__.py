# -*- coding: utf-8 -*-
{
    'name': 'Gestión de Nóminas',
    'version': '18.0.1.0.0',
    'summary': 'Gestión sencilla de nóminas y declaraciones anuales',
    'description': """
Módulo académico para gestionar nóminas, bonificaciones, deducciones e IRPF
y generar la declaración de renta anual de cada empleado.
    """,
    'author': 'Joaquin Carrasco',
    'website': 'https://github.com/JoaquinCarrasco',
    'category': 'Human Resources/Payroll',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/tax_return_views.xml',
        'views/payroll_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
