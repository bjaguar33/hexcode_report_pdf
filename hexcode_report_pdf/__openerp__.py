{
    'name': 'Report PDF',
    'version': '1.0',
    'category': 'app',
    'description': 'HexCode pdf Report is a module that allows the creation of professional reports and can download them in PDF format. It currently supports pdf report for: Claims, Invoice, Sales Order, Quotations, Picking, Request for Quotations and Purchase Orders.',
    'summary': 'Module for creating professional PDF reports',
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
