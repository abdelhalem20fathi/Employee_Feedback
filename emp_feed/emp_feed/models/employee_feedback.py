from odoo import models, fields, api
from odoo.exceptions import UserError
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
    ], string='Category',required=True)
    attachment_ids = fields.Many2many('ir.attachment', string='Attachments')
    rating = fields.Integer(string="Rating", default=0)

    attachment_ids = fields.Many2many(
        'ir.attachment', string='Attachments',
        help="Attach documents, images, or other files related to the feedback."
    )
    rating = fields.Integer(string='Rating', required=True, default=1)

    # Field Constraints
    _sql_constraints = [
        ('check_rating_range', 'CHECK(rating >= 1 AND rating <= 5)',
         'Rating must be between 1 and 5 stars.')
    ]



class Employee(models.Model):
    _inherit = 'hr.employee'

    feedback_ids = fields.One2many('employee.feedback', 'employee_id', string='Feedback')




