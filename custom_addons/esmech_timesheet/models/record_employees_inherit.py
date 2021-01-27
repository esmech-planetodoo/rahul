from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


class EmployeeRecord(models.Model):
    """ Employee records """

    _name = 'hr.employee'
    _inherit = 'hr.employee'
    _description = 'Employee Details'

    personalinfo_data_ids = fields.One2many('employee.info.data', 'employee_records_id', string='Personal information')
    employee_location_ids = fields.One2many('employee.location', 'employee_records_id', string='Location Information')
    employee_job_ids = fields.One2many('employee.job', 'employee_records_id', string='Job Information')
    employee_experience_ids = fields.One2many('employee.experience', 'employee_records_id', string='Experience')
    qualification_ids = fields.One2many('employee.qualification', 'employee_records_id', string='Qualification')
    bankinfo_ids = fields.One2many('employee.bankinfo', 'employee_records_id', string='Bank Information')
    name = fields.Char("Name", related="full_name")
    first_name = fields.Char("First Name")
    middle_name = fields.Char("Middle Name")
    last_name = fields.Char("Last Name")
    full_name = fields.Char(string="Full Name", store=True, compute="_full_name")
    organization = fields.Char("Organization", required="True")
    employee_roll_no = fields.Char("Employee Id", default="0000")
    card_no = fields.Char("Card No", default="0011096340")
    email = fields.Char("Email")
    alter_email = fields.Char("Alternate Email")
    work_phone = fields.Char("Phone No.")
    mobile_phone = fields.Char("Mobile No.")
    alter_phone = fields.Char("Alternate Phone No.")
    emergency_contact = fields.Char("Emergency Contact No.")
    image = fields.Binary("Image")
    description = fields.Char("Description")
    is_active = fields.Boolean("Active")
    shift = fields.Boolean("Shift")
    rotation = fields.Selection([
        ('half_monthly', 'Half Monthly'),
        ('monthly', 'Monthly'),
        ('weekly', 'Weekly'),
    ], string='Rotation')
    business_partner = fields.Char("Business Partner")
    user_contact = fields.Char("User/Contact")
    add_data = fields.Char("ADD Data")

    creation_date = fields.Char("Creation Date")
    created_by = fields.Char("Created By")
    updated = fields.Char("Updated")
    updated_by = fields.Char("Updated By")

    notes = fields.Text("Notes")

    @api.depends('first_name', 'middle_name', 'last_name')
    def _full_name(self):
        for record in self:
            record.full_name = (record.first_name or '') + ' ' + (record.middle_name or '') + ' ' + (
                    record.last_name or '')


class PersonalInformationData(models.Model):
    _name = 'employee.info.data'
    _description = 'Personal Information Data'
    _order = 'employee_name'

    employee_records_id = fields.Many2one('hr.employee')
    employee_name = fields.Char("Employee")
    father_name = fields.Char("Father Name")
    mother_name = fields.Char("Mother Name")
    nick_name = fields.Char("Nick Name")
    spouse_name = fields.Char("Spouse Name")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], groups="hr.group_hr_user", tracking=True)
    marital = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('cohabitant', 'Legal Cohabitant'),
        ('widower', 'Widower'),
        ('divorced', 'Divorced')
    ], string='Marital Status', groups="hr.group_hr_user", default='single', tracking=True)
    birthday = fields.Date('Date of Birth', groups="hr.group_hr_user", tracking=True)
    age = fields.Char("Age")
    place_birth = fields.Char("Place of Birth")
    blood_group = fields.Char("Blood Group")
    religion = fields.Char("Religion")
    dependent_no = fields.Char("No. of Dependents")
    country_id = fields.Many2one('res.country', string="Citizenship")
    ethnic_race = fields.Char("Ethnic Race")
    pf_no = fields.Char("PF/EPF No.")
    driving_lic = fields.Char("Driving License No.")
    dl_issue_date = fields.Date("Driving License Issue Date")
    dl_expiry_date = fields.Date("Driving License Expiry Date")
    pan_no = fields.Char("PAN No.")
    passport_no = fields.Char("Passport No.")
    passport_issue_date = fields.Date("Passport Issue Date")
    passport_expiry_date = fields.Date("Passport Expiry Date")
    esi_no = fields.Char("ESI No.")
    uid_no = fields.Char("Unique Identity Card No.")
    is_active = fields.Boolean("Active")


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
    emp_department_id = fields.Many2one('employee.department', "Employee Category")
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
    employee_name = fields.Char("Employee")
    prev_employer = fields.Char("Previous Employer")
    designation = fields.Char("Designation")
    date_of_join = fields.Date("Date of Join")
    salary = fields.Char("Salary")
    relieved_date = fields.Date("Relieved Date")
    reason_for_relieving = fields.Char("Reason for Relieving")
    is_active = fields.Boolean("Active")


# Qualification Experience section
class EmployeeQualification(models.Model):
    """ Model for Child Educational qualification """

    _name = 'employee.qualification'
    _description = 'Employee Educational qualification'

    employee_records_id = fields.Many2one('hr.employee')
    employee_name = fields.Char("Employee")
    degree = fields.Char("Degree")
    specialisation = fields.Char("Specialisation")
    institute = fields.Char("Institute")
    university = fields.Char("University")
    year_of_pass = fields.Char("Year of Passing")
    percentage = fields.Char("Percentage")


# Bank info section
class EmployeeBankInfo(models.Model):
    """ Model for Child Educational qualification """

    _name = 'employee.bankinfo'
    _description = 'Employee Bank Account Details'

    employee_records_id = fields.Many2one('hr.employee')
    employee_name = fields.Char("Employee")
    account_no = fields.Char("Account No.")
    account_name = fields.Char("Account Name")
    bank_name = fields.Char("Bank Name")
    branch_name = fields.Char("Branch Name")
    description = fields.Char("Description")
    default = fields.Char("Default")