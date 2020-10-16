from odoo import tools
from odoo import models, fields


class LoanRequest(models.Model):
    _name = 'loan.request'
    _description = 'Loan Request Form'

    first_name = fields.Char()
    employee_id = fields.Many2one("hr.employee", string="Employee Name", required=False, )
    advance_type=new_field = fields.Char(string="Advance Type", required=False, )

