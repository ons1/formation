# -*- coding: utf-8 -*-

{
    'name': 'Formation technique odoo v8',
    'version': '1.0',
    'author': 'Khemiri Ons',
    'website': 'https://www.sdatacave.com',
    'support': 'onskhemiri@gmail.com',
    'license': "AGPL-3",
    'complexity': 'easy',
    'sequence': 1,
    'category': 'category',
    'description': """
        Put your description here for your module:
            - model1
            - model2
            - model3
    """,
    'depends': ['base','mail','hr'],
    'summary': 'Formation, odoo8, odoo11',
    'data': [
        'security/formation.xml',
        'security/ir.model.access.csv',
        #'data/ModuleName_data.xml',
        'views/formation_views.xml',
        'views/formation_inherit.xml',
        'wizard/wiz_views.xml',
        'report/registration.xml',
        'report/report.xml',
        'menu_view.xml',
        'data/sequence.xml',
        'demo/demo.xml',
        
    ],
    'demo': [
        #'demo/ModuleName_demo.xml'
    ],
    'css': [
        #'static/src/css/ModuleName_style.css'
    ],
    
    'price': 100.00,
    'currency': 'EUR',
    'installable': True,
    'application': True,
}
