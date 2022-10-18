from odoo import api, fields, models, _


class Partner(models.Model):
    _inherit = 'res.partner'

    khmer_name = fields.Char(string="Khmer Name", copy=False, tracking=True)
