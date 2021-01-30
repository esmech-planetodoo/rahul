from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.addons.test_impex.tests.test_load import test_required_string_field
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


# Employee job section
class EmployeeJob(models.Model):
    _name = 'employee.job'
    _description = 'Employee work details'

    employee_records_id = fields.Many2one('hr.employee')
    payment_method_id = fields.Many2one('employee.payment.method', "Payment Method")
    employee_name = fields.Char("Employee")
    financial_acc = fields.Char("Financial Account")
    weekly_off_id = fields.Many2one('employee.weekly.off', "Define Weekends")
    work_shift_id = fields.Many2one('employee.work.shift', "Work Shift")
    designation_id = fields.Many2one('employee.designation', "Designation/Position")
    team_id = fields.Many2one('employee.team', "Team")
    pay_grade_id = fields.Many2one('employee.pay.grade', "Pay Grade")
    emp_category_id = fields.Many2one('employee.category', "Employee Category")
    emp_department_id = fields.Many2one('employee.department', "Employee Department")
    date_joining = fields.Date("Date of Joining")
    years_service = fields.Char("Years Of Service")
    probation_period = fields.Char("Probation Period")
    confirmation_date = fields.Date("Confirmation Date")
    retirement_date = fields.Date("Retirement Date")
    relieved_date = fields.Date("Relieved Date")
    reason_leaving = fields.Char("Reason for Leaving")
    leave_policy_id = fields.Many2one('employee.leave.policy', "Leave Policy")
    is_active = fields.Char("Active")


class PaymentMethod(models.Model):
    _name = 'employee.payment.method'
    _description = 'Payment Method Class'
    _rec_name = 'name'

    name = fields.Char("Name")
    description = fields.Char("Description")
    is_active = fields.Boolean("Active")


# To Be taken care of later as field are already empty
# class FinancialAccount(models.Model):
#     _name = 'employee.account.financial'
#     _description = 'Employee financial account'


class WeeklyOff(models.Model):
    _name = 'employee.weekly.off'
    _description = 'Employee weekly off'

    monday = fields.Boolean("Monday")
    tuesday = fields.Boolean("Tuesday")
    wednesday = fields.Boolean("Wednesday")
    thursday = fields.Boolean("Thursday")
    friday = fields.Boolean("Friday")
    saturday = fields.Boolean("Saturday")
    sunday = fields.Boolean("Sunday")


class WorkShift(models.Model):
    _name = 'employee.work.shift'
    _description = 'Employee work shift'
    _rec_name = 'name'

    search_key = fields.Char("Search Key")
    name = fields.Char("Name")
    starting_time = fields.Float("Starting Time")
    ending_time = fields.Float("Ending Time")
    duration = fields.Float("Duration")
    ot_applicable = fields.Boolean("OT Applicable")
    description = fields.Char("Description")
    is_active = fields.Boolean("Active")


class Designation(models.Model):
    _name = 'employee.designation'
    _description = 'Employee Designation'

    search_key = fields.Char("Search Key")
    name = fields.Char("Name")
    description = fields.Char("Description")
    is_active = fields.Boolean("Active")
    is_compoff = fields.Boolean("Comp Off")


class Team(models.Model):
    _name = 'employee.team'
    _description = 'Employee work details'

    search_key = fields.Char("Search Key")
    name = fields.Char("Name")
    reporting_manager = fields.Char("Reporting Manager")
    description = fields.Char("Description")
    is_active = fields.Boolean("Active")
    is_include = fields.Boolean("Is Include in Timesheet Report")


class PayGrade(models.Model):
    _name = 'employee.pay.grade'
    _description = 'Employee Pay Grade'

    search_key = fields.Char("Search Key")
    name = fields.Char("Name")
    encash_leave = fields.Char("Encash Leave Cost Per Day")
    overtime_per_hrs = fields.Float("Overtime per hour")
    formulae = fields.Float("Formula")
    min_salary = fields.Float("Minimum Salary")
    max_salary = fields.Float("Maximum Salary")
    description = fields.Char("Description")
    is_active = fields.Boolean("Active")


class EmployeeCategory(models.Model):
    _name = 'employee.category'
    _description = 'Employee category'

    search_key = fields.Char("Search Key")
    name = fields.Char("Name")
    description = fields.Char("Description")
    is_active = fields.Boolean("Active")


class EmployeeDepartment(models.Model):
    _name = 'employee.department'
    _description = 'Employee Department'

    search_key = fields.Char("Search Key")
    name = fields.Char("Name")
    description = fields.Char("Description")
    is_active = fields.Boolean("Active")


class LeavePolicy(models.Model):
    _name = 'employee.leave.policy'
    _description = 'Employee Leave policy'

    search_key = fields.Char("Search Key")
    name = fields.Char("Name")
    valid_from = fields.Date("Valid from Date")
    leave_allocation = fields.Char("Field Allocation")  # Different Class
    is_probation = fields.Boolean("Under Probation")


# Employee Experience section
class EmployeeExperience(models.Model):
    """ Model for Child Work Experience Information """

    _name = 'employee.experience'
    _description = 'Employee Work Experience Information'

    employee_records_id = fields.Many2one('hr.employee')
    employee_name = fields.Char("Employee", readonly=True)
    prev_employer = fields.Char("Previous Employer", required=True)
    designation = fields.Char("Designation")
    date_of_join = fields.Date("Date of Join")
    salary = fields.Char("Salary")
    relieved_date = fields.Date("Relieved Date")
    reason_for_relieving = fields.Char("Reason for Relieving")
    is_active = fields.Boolean("Active")
