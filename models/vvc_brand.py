from odoo import models, fields

class Brand(models.Model):
    _name = 'vvc.brand'
    
    name = fields.Char(string="Brand", required=True)
    certificates_id = fields.One2many(comodel_name="vvc.certificates", inverse_name="brand" , string='Certificates',ondelete='cascade')