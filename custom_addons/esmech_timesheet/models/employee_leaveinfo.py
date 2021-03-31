from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.addons.test_impex.tests.test_load import test_required_string_field
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


# Leave Info section
class EmployeeLeaveInfo(models.Model):
    """ Model for Child Leave Information """

    _name = 'employee.leaveinfo'
    _description = 'Employee Leave Information'

    employee_records_id = fields.Many2one('hr.employee.master')
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

    employee_records_id = fields.Many2one('hr.employee.master')
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

    employee_records_id = fields.Many2one('hr.employee.master')
    shift_schedule = fields.Char("Shift schedule")
    start_day = fields.Char("Start day")
    end_day = fields.Char("End day")
    rotation = fields.Char("Shift Rotation", required=True)
    employee_name = fields.Char("Employee", readonly=True)
    description = fields.Char("Description")


class AttendanceStatus(models.Model):
    _name = 'attendance.status'
    _description = 'Employee attendance status in public conference and checking employees daily company attendance.'
    _rec_name = 'name'

    name = fields.Char("Name")
    is_weekend = fields.Boolean("Weekend")
    is_default = fields.Boolean("Absent")
    is_present = fields.Boolean("Present")
    is_compoff = fields.Boolean("Comp Off")
    is_holiday = fields.Boolean("Holiday")
    is_leave = fields.Boolean("Leave")
    is_lop = fields.Boolean("LOP")
    is_ot = fields.Boolean("OT")
    is_halfday = fields.Boolean("Half Day")
    maternity = fields.Char("Maternity")
    description = fields.Char("Description")
    is_ontour = fields.Boolean("On Tour")
    is_wow = fields.Boolean("Worked On Weekend")
    is_short = fields.Boolean("Short Leave")
    is_active = fields.Boolean("Active")


class LeaveType(models.Model):
    _name = 'leave.type'
    _description = 'Different reasons for staying away from the work place, like sick leave, casual leave etc.,'
    _rec_name = 'name'

    is_encashable = fields.Boolean("Encashable")
    leave_category = fields.Selection([
        ('comp_off', 'Comp Off'),
        ('paid_leave', 'Paid Leave'),
        ('short_leave', 'Short Leave'),
        ('unpaid_leave', 'Unpaid Leave'),
    ], string="Leave Category")
    #    description = fields.Boolean("Description")
    name = fields.Char("Name")
    is_earned = fields.Boolean("Earned")
    is_autocredit = fields.Boolean("Auto Credit")
    org_id = fields.Boolean("Organization")
    maternity_leave_id = fields.Boolean("Maternity Leave")
    is_active = fields.Boolean("Active")
    maternity = fields.Boolean("Maternity")
    leave_laps_days = fields.Char("Leave Lapse After (Days)")
    is_esi = fields.Boolean("ESI")
