from odoo import models, fields

class CertificateTypes(models.Model):
    _name = 'vvc.ctypes'
    
    name = fields.Char(string="Certificate Type", required=True)
    certificates_id = fields.One2many(comodel_name="vvc.certificates", inverse_name="ctypes_name" , string='Certificates',ondelete='cascade')