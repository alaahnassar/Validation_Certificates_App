from odoo import models, fields

class TrafficDepartment(models.Model):
    _name = 'vvc.tdepartment'
    
    name = fields.Char(string="Traffic Department", required=True)
    certificates_id = fields.One2many(comodel_name="vvc.certificates", inverse_name="tdepartment_name" , string='Certificates',ondelete='cascade')