{
    'name': 'Report PDF',
    'version': '1.0',
    'category': 'app',
    'description': '',
    'author': 'Federico Ranieri',
    'website': 'www.federicoranieri.it',
    'depends': [
        'base', 'base_setup', 'report', 'crm_claim', 'sale', 'account', 'stock', 'purchase'
    ],
    'data': [
        'hexcode_report.xml',
        'hexcode_report_pdf_settings.xml'
    ],
    'installable': True,
    'auto_install': False,
    'price': 98,
    'currency': 'EUR',
    'images': ['images/main_screenshot.png'],
    'css': ['static/src/css/style.css'],
}