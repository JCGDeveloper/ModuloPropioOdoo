# -*- coding: utf-8 -*-
{
    'name': 'Paquetería - Gestión de paquetes y flota',
    'version': '1.0',
    'summary': 'Gestión de paquetes, seguimiento y camiones',
    'description': """
        Módulo para gestionar:
        - Paquetes con remitente, destinatario y dirección
        - Seguimiento de cada paquete con estado y notas
        - Camiones de la flota y sus conductores
    """,
    'author': 'Tu Nombre',
    'category': 'Operations/Logistics',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/paquete_views.xml',
        'views/seguimiento_views.xml',
        'views/camion_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
