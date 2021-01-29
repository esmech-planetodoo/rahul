from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.addons.test_impex.tests.test_load import test_required_string_field
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


class EmployeeLocation(models.Model):
    _name = 'employee.location'
    _description = 'Employee residential details'

    employee_records_id = fields.Many2one('hr.employee')
    employee_name = fields.Char("Employee")
    company_id = fields.Many2one(
        'res.company', string='Company', change_default=True,
        default=lambda self: self.env.company,
        required=False, invisible=True)
    address_id = fields.Many2one('res.partner', 'Location/Address', compute="_compute_address_id", store=True,
                                 readonly=False, )
    present_address = fields.Boolean("Present")
    permanent_address = fields.Boolean("Permanent")
    default = fields.Boolean("Default")
    is_active = fields.Boolean("Active")
    location_type = fields.Selection([
        ('metropolitan', 'Metropolitan'),
        ('non_metropolitan', 'Non Metropolitan'),
    ], string='Location Type')

    @api.depends('company_id')
    def _compute_address_id(self):
        for employee in self:
            address = employee.company_id.partner_id.address_get(['default'])
            employee.address_id = address['default'] if address else False