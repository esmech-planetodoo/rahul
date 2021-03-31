from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.addons.test_impex.tests.test_load import test_required_string_field
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


class PersonalInformationData(models.Model):
    _name = 'employee.info.data'
    _description = 'Personal Information Data'
    _order = 'employee_name'

    employee_records_id = fields.Many2one('hr.employee.master')
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

    employee_records_id = fields.Many2one('hr.employee.master')
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


# Qualification Qualification section
class EmployeeQualification(models.Model):
    """ Model for Child Educational qualification """

    _name = 'employee.qualification'
    _description = 'Employee Educational qualification'

    employee_records_id = fields.Many2one('hr.employee.master')
    employee_name = fields.Char("Employee", readonly=True)
    degree = fields.Char("Degree", required=True)
    specialisation = fields.Char("Specialisation")
    institute = fields.Char("Institute")
    university = fields.Char("University")
    year_of_pass = fields.Char("Year of Passing")
    percentage = fields.Char("Percentage")
    is_active = fields.Boolean("Active")


# Bank info section
class EmployeeBankInfo(models.Model):
    """ Model for Child Educational qualification """

    _name = 'employee.bankinfo'
    _description = 'Employee Bank Account Details'

    employee_records_id = fields.Many2one('hr.employee.master')
    employee_name = fields.Char("Employee", readonly=True)
    account_no = fields.Char("Account No.", required=True)
    account_name = fields.Char("Account Name", required=True)
    bank_name = fields.Char("Bank Name", required=True)
    branch_name = fields.Char("Branch Name", readonly=True)
    description = fields.Char("Description", readonly=True)
    default = fields.Char("Default")


class UserContact(models.Model):
    _name = 'employee.user.contact'
    _description = 'User/Contact'
    _rec_name = 'name'

    #FIXME : Create view for class
    organization_id = fields.Many2one('organization.master', "Organization")
    name = fields.Char("Name")
    description = fields.Text("Description")
    password = fields.Char("Password")
    is_active = fields.Boolean("Active")
    client_id = fields.Char("Client")
    email = fields.Char("email")
    supervisor_id = fields.Char("Supervisor")
    partner_id = fields.Char("Business Partner")
    email_server_user = fields.Char("Email Server Username")
    email_server_password = fields.Char("Email Server Password")
    alt_phone = fields.Char("Alternative Phone")
    birthday = fields.Char("Birthday")
    partner_location_id = fields.Char("Partner Address")
    phone = fields.Char("Phone")
    fax = fields.Char("Fax")
    position = fields.Char("Position")
    first_name = fields.Char("First Name")
    last_name = fields.Char("Last Name")
    user_name = fields.Char("User Name")
    default_client_id = fields.Char("Default Client")
    default_organization_id = fields.Char("Default Organization")
    default_language_id = fields.Char("Default Language")
    default_role_id = fields.Char("Default Role")
    default_warehouse_id = fields.Char("Default Warehouse")
    is_locked = fields.Boolean('Locked')
