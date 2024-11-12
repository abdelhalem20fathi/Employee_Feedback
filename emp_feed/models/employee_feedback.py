from odoo import models, fields, api

from odoo17.odoo.exceptions import ValidationError


class EmployeeFeedback(models.Model):
    _name = 'employee.feedback'
    _description = 'Employee Feedback'

    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    feedback = fields.Text(string="Feedback", required=True)
    date_submitted = fields.Date(string="Date Submitted", default=fields.Date.today)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('action_taken', 'Action Taken')
    ], string="Status", default='pending')


    category = fields.Selection([
        ('work_environment', 'Work Environment'),
        ('management', 'Management'),
        ('team_dynamics', 'Team Dynamics')
    ], string='Category')
    attachment_ids = fields.Many2many('ir.attachment', string='Attachments')
    rating = fields.Integer(string="Rating", default=0)

class Employee(models.Model):
    _inherit = 'hr.employee'

    feedback_ids = fields.One2many('employee.feedback', 'employee_id', string='Feedback')




