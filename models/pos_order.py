from odoo import models, fields

class PosOrder(models.Model):
    _inherit = 'pos.order'

    app_trans_id = fields.Char(string="Mã Giao Dịch ZaloPay")
