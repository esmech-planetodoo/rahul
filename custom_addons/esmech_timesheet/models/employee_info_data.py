from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.addons.test_impex.tests.test_load import test_required_string_field
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


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
