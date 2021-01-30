from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.addons.test_impex.tests.test_load import test_required_string_field
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


# Leave Info section
class EmployeeLeaveInfo(models.Model):
    """ Model for Child Leave Information """

    _name = 'employee.leaveinfo'
    _description = 'Employee Leave Information'

    employee_records_id = fields.Many2one('hr.employee')
    employee_name = fields.Char("Employee", required=True)
    leave_type = fields.Char("Leave Type", required=True)
    available_leaves = fields.Char("Available Leaves", required=True)
    encashed_leaves = fields.Char("Encashed Leaves", required=True)
    leaves_taken = fields.Char("Leaves Taken", required=True)
    accured = fields.Date("Accrued For Month Year(MM-YYYY)")


# Leave Details section
class EmployeeLeaveDetails(models.Model):
    """ Model for Child Leave Details """

    _name = 'employee.leave.details'
    _description = 'Employee Leave Details'

    employee_records_id = fields.Many2one('hr.employee')
    leave = fields.Char("Leave Date")
    reason = fields.Char("Reason")
    leave_requisition = fields.Char("Leave Requisition")
    employee_punch = fields.Char("Employee Punch")
    leave_status = fields.Char("Leave Status")
    accured_on = fields.Char("Accrued On")
    valid_till = fields.Char("Valid Till Date")
    avail_leaves = fields.Char("Available Leaves")


class EmployeeShift(models.Model):
    """ Model for Child Shift Details """

    _name = 'employee.shift'
    _description = 'Employee Shift Details'

    employee_records_id = fields.Many2one('hr.employee')
    shift_schedule = fields.Char("Shift schedule")
    start_day = fields.Char("Start day")
    end_day = fields.Char("End day")
    rotation = fields.Char("Shift Rotation", required=True)
    employee_name = fields.Char("Employee", readonly=True)
    description = fields.Char("Description")
