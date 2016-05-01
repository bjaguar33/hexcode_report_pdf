from openerp import fields,models

class hexcode_report_pdf(models.Model):
    _name = "hexcode_report_pdf"

    description = fields.Char(string="Descrizione", default="Plugin Hexcode Report PDF V.1.0, Clicca su Crea per aggiungere una nuova regola di stile. All'interno"
                                                            "dei form dei: preventivi, claim etc.. troverai un campo dove potrai selezionare una regola di stile creata.")
    name = fields.Char(string="Nome Regola")

    stile = fields.Selection([('theme_one', 'Green Theme'),
                              ('theme_two', 'Blue Theme'),
                              ('theme_three', 'Orange Theme'),
                              ('theme_four', 'Red Theme'),
                              ('theme_five', 'Azure Theme'),
                              ('theme_six', 'Yellow Theme')])


class hexcode_report_pdf_claim(models.Model):
    _inherit = "crm.claim"

    hexcode_report_pdf = fields.Many2one("hexcode_report_pdf", string="Layout Report PDF", required=True)

class hexcode_report_pdf_quotation(models.Model):
    _inherit = "sale.order"

    hexcode_report_pdf = fields.Many2one("hexcode_report_pdf", string="Layout Report PDF", required=True)

class hexcode_report_pdf_invoice(models.Model):
    _inherit = "account.invoice"

    hexcode_report_pdf = fields.Many2one("hexcode_report_pdf", string="Layout Report PDF", required=True)

class hexcode_report_pdf_picking(models.Model):
    _inherit = "stock.picking"

    hexcode_report_pdf = fields.Many2one("hexcode_report_pdf", string="Layout Report PDF", required=True)

class hexcode_report_pdf_purchase(models.Model):
    _inherit = "purchase.order"

    hexcode_report_pdf = fields.Many2one("hexcode_report_pdf", string="Layout Report PDF", required=True)

hexcode_report_pdf()
hexcode_report_pdf_claim()
hexcode_report_pdf_quotation()
hexcode_report_pdf_invoice()
hexcode_report_pdf_picking()
hexcode_report_pdf_purchase()