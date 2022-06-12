{
    'name': "purchase request custom",
    'version': '1.0',
    'depends': ['purchase_request'],
    'author': "Daten S.A.S.",
    'category': 'compras',
    'description': "oculta campo grupo de abastecimiento",
    # data files always loaded at installation
    'data': ["views/inherited_purchase_request.xml",
             "views/inherited_purchase_order.xml",
            ],
    # data files containing optionally loaded demonstration data
    'demo': [],
    "license": "LGPL-3",
    "installable": True,
    "application": True,
}