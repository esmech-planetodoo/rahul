from odoo import models, fields, api
from datetime import datetime, timedelta


class Student(models.Model):
    _name = 'students.details'
    _description = 'student details'
    education_ids = fields.One2many('education.details', 'student_ids', "Education")
    library_ids = fields.Many2one('library.details', "student class")

    first_name = fields.Char("First Name", required=True, default="First")
    last_name = fields.Char("Last Name", required=True, default="Last")
    full_name = fields.Char("Full Name", compute='_full_name')
    roll_number = fields.Integer("Roll Number", required=True)
    gender = fields.Selection([('M', 'Male'), ('F', 'Female')], "Gender")
    dob = fields.Date("Date of birth")
    age = fields.Integer("Age", compute='_age_count', default=17)
    phone = fields.Char("Phone Number")
    email = fields.Char("e-mail")
    reading = fields.Boolean("Reading", default=False)
    swimming = fields.Boolean("Swimming", default=False)
    dancing = fields.Boolean("Dancing", default=False)

    # Compute fields

    @api.depends('first_name', 'last_name')
    def _full_name(self):
        for record in self:
            record.full_name = str(record.first_name) + " " + str(record.last_name)

    @api.depends('dob')
    def _age_count(self):
        self.age = 0
        for record in self:
            if record.dob is not False:
                record.age = (datetime.today().date() - datetime.strptime(str(record.dob),
                                                                          '%Y-%m-%d').date()) // timedelta(days=365)


class Education(models.Model):
    _name = 'education.details'
    _description = 'student marks details'
    student_ids = fields.Many2one('students.details', "Main Class")

    chemistry_marks = fields.Float("Chemistry")
    physics_marks = fields.Float("Physics")
    maths_marks = fields.Float("Maths")
    english_marks = fields.Float("English")
    total_marks = fields.Float("Total Marks", compute='_marks_total')
    percentage = fields.Integer("Percentage", compute='_marks_percentage')
    status = fields.Char("Status", compute='_status')

    # Compute fields

    @api.depends('chemistry_marks', 'physics_marks', 'maths_marks', 'english_marks')
    def _marks_total(self):
        self.total_marks = 0
        for record in self:
            record.total_marks = record.chemistry_marks + record.physics_marks \
                                 + record.maths_marks + record.english_marks

    @api.depends('total_marks')
    def _marks_percentage(self):
        self.percentage = 0
        for record in self:
            record.percentage = (record.total_marks / 400) * 100

    @api.depends('percentage')
    def _status(self):
        for record in self:
            if record.percentage < 40:
                record.status = 'Fail'
            else:
                record.status = 'Pass'
