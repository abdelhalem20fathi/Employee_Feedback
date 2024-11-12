{
    'name': 'Employee Feedback',
    'version': '1.0',
    'category': 'Human Resources',

    'summary': 'Module for Employee Feedback',
    'description': 'Allows employees to submit feedback, with review options for managers.',
    'author': 'Abdelhalem Fathi',
    'depends': ['base', 'hr'],
    'data': [

        'security/ir.model.access.csv',
        'views/employee_feedback_view.xml',
        'security/employee_feedback_security.xml',
        'views/employee_view.xml',
        'views/basetodo_menu.xml',
    ],
    'installable': True,
    'application': True,
}
