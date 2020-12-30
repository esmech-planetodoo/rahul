from odoo import models, fields, api


class Teacher(models.Model):
    # _name = "teacher.details"
    # _description = "books issued in library details"
    _inherit = 'res.partner'

    teacher_name = fields.Char("Teachers Name")
    salary = fields.Float("salary")

