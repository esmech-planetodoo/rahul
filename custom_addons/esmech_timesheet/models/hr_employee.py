from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.addons.test_impex.tests.test_load import test_required_string_field
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


class EmployeeRecord(models.Model):
    """ Employee records """

    _name = 'hr.employee.master'
    _inherit = ['hr.employee', 'image.mixin']
    _description = 'Employee Details'
    _rec_name = 'full_name'

    @api.model
    def _default_image(self):
        image_path = get_module_resource('hr', 'static/src/img', 'default_image.png')
        return base64.b64encode(open(image_path, 'rb').read())

    personalinfo_data_ids = fields.One2many('employee.info.data', 'employee_records_id', string='Personal information')
    employee_location_ids = fields.One2many('employee.location', 'employee_records_id', string='Location Information')
    employee_job_ids = fields.One2many('employee.job', 'employee_records_id', string='Job Information')
    employee_experience_ids = fields.One2many('employee.experience', 'employee_records_id', string='Experience')
    qualification_ids = fields.One2many('employee.qualification', 'employee_records_id', string='Qualification')
    bankinfo_ids = fields.One2many('employee.bankinfo', 'employee_records_id', string='Bank Information')
    leaveinfo_ids = fields.One2many('employee.leaveinfo', 'employee_records_id', string='Leave Information')
    employeeleave_ids = fields.One2many('employee.leave.details', 'employee_records_id', string='Employee Leave details')
    employeeshift_ids = fields.One2many('employee.shift', 'employee_records_id', string='Employee Shift details')
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
    image_1920 = fields.Image(default=_default_image)

    creation_date = fields.Char("Creation Date")
    created_by = fields.Char("Created By")
    updated = fields.Char("Updated")
    updated_by = fields.Char("Updated By")

    notes = fields.Text("Notes")
    #category field to remove delegation
    # category_ids = fields.Many2many(
    #     'hr.employee.category', 'employee_category_rel',
    #     'emp_id', 'category_id', groups="hr.group_hr_manager",
    #     string='Tags')


    @api.depends('first_name', 'middle_name', 'last_name')
    def _full_name(self):
        for record in self:
            record.full_name = (record.first_name or '') + ' ' + (record.middle_name or '') + ' ' + (
                    record.last_name or '')

    class EmployeeRecord(models.Model):
        """ Employee records """

        _name = 'hr.employee.category'

        employee_ids = fields.Many2many('hr.employee.master', 'employee_category_rel', 'category_id', 'emp_id',
                                        string='Employees')
