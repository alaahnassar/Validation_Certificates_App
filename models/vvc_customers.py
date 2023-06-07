from odoo import models, fields

class Customers(models.Model):
    _name = 'vvc.customers'
    
    name = fields.Char(string="Name", max_length=50, required=True)
    phone = fields.Char(string="Phone", required=True)
    # certificates_id = fields.One2many(comodel_name="vvc.certificates", inverse_name="customer_name" , string='Certificates',ondelete='cascade')
