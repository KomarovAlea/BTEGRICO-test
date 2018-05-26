# -*- coding: utf-8 -*-
{
    'name': 'Task 4',
    'version': '11.0.1.0',
    'author': "Oleksandr Komarov",
    'website': 'https://modool.pro',
    'summary': '',
    'description': """
SQl запрос в базу данных PSQL Odoo, выборка всех подписчиков канала 'general', 
которое подписались на канал в этом месяце. Запрос возвращает 
ид, имя и мейл подписчика, дату подписки.
    """,
    'category': 'Base',
    'depends': ['mail'],
    'data': [
        'views/mail_channel_views.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
