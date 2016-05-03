from openerp import fields,models

class hexcode_report_pdf(models.Model):
    _name = "hexcode_report_pdf"

    description = fields.Char(readonly=True, default="Plugin HEXCode PDF Report V.1.0, Click Create to add a new style rule. Within the form of: preventive, claim etc .. will be a box where you can select a style rule created.")
    name = fields.Char()

    stile = fields.Selection([('theme_one', 'Green Theme'),
                              ('theme_two', 'Blue Theme'),
                              ('theme_three', 'Orange Theme'),
                              ('theme_four', 'Red Theme'),
                              ('theme_five', 'Azure Theme'),
                              ('theme_six', 'Yellow Theme')])

    is_custom_report = fields.Boolean(default=False)
    main_color = fields.Char(default="#16a085")
    secondary_color = fields.Char(default="#16a085")
    text_color_primary = fields.Char(default="#16a085")
    text_color_secondary = fields.Char(default="#16a085")

    text_size = fields.Integer(default=14)

    footer_color = fields.Char(default="#16a085")
    footer_color_text = fields.Char(default="#16a085")
    header_color = fields.Char(default="#16a085")
    header_color_text = fields.Char(default="#16a085")


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