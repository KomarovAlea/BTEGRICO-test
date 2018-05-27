# -*- coding: utf-8 -*-
{
    'name': 'Task 6',
    'version': '11.0.1.0',
    'author': "Oleksandr Komarov",
    'website': 'https://modool.pro',
    'summary': '',
    'description': """
Добавить в продукт поля для описания товара: Состав, Применение, Особенности - 
содержание данных полей выводится на страницу магазина.
    """,
    'category': 'Base',
    'depends': ['website_sale'],
    'data': [
        'views/product_views.xml',
        'views/product_templates.xml'
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
