# -*- coding: utf-8 -*-
{
    'name': 'Task 3',
    'version': '11.0.1.0',
    'author': "Oleksandr Komarov",
    'website': 'https://modool.pro',
    'summary': '',
    'description': """
В модуле закупок (purchase) на партнера установить домейн так
чтоб для выбора были доступны только компании что имеют у себя тег 'it'.
    """,
    'category': 'Base',
    'depends': ['base', 'purchase'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
