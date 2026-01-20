{
    'name': 'PC Inventory',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Gestión de ordenadores y componentes',
    'description': """
        Gestión de Inventario de PC
        ============================
        
        Este módulo permite gestionar:
        - Componentes de ordenadores
        - Ordenadores de la empresa
        - Asignación de usuarios
        - Precios y mantenimiento
    """,
    'author': 'Joaquin',
    'website': 'https://www.example.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/component_views.xml',
        'views/computer_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}


