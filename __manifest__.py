# -*- coding: utf-8 -*-
{
    'name': "Hamasat",
    'summary': """
        Summaey Hamasat""",

    'description': """
        A charity project that does not rely on non-core Odoo modules.
    """,
    'author': "Abdalla alsafy",
    'website': "http://www.Faceboock.com/abdalla6alsafy",
    'category': 'Uncategorized',
    'version': '13.0.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/persones.xml',
        'views/zones.xml',
        'views/sones_adj.xml',
        'views/person_files.xml',
        'views/kashf.xml',
        'reports/cards.xml',
        'views/templates.xml',
        'demo/sones_adj.xml',
        'wizards/degree.xml',
    ],
    'demo': [],
}
