# -*- coding: utf-8 -*-
{
    'name': "exe_debit_note_fix",

    'summary': """
        Parche para estabilizar la vista del boton nota debito.""",

    'description': """
        
    """,

    'author': "Exemax",
    'website': "http://www.exemax.com.ar",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '18.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account', 'account_debit_note'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    
}
