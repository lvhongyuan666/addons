# -*- coding: utf-8 -*-
{
    'name': "自动生成单据编号",

    'summary': '',

    'description': """
功能
====
* 创建一条单据，自动生成单据编号
""",

    'author': "lhy",
    'website': "",
    'category': 'workbench',
    'version': '1.0',
    'installable': True,
    'license': 'LGPL-3',
    'depends': ['base'],

    # always loaded
    'data': [
        'data/sequence.xml',
        'views.xml',


    ],
}
