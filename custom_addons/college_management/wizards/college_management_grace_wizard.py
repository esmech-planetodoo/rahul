# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class GraceWizard(models.TransientModel):
    _name = 'college.management.grace.wizard'
    _description = 'add grace to total marks'

    grace_marks = fields.Float("Grace Marks")

    def add_marks(self):
        active_ids = self._context.get('active_ids') or self._context.get('active_id')
        education_id = self.env['education.details'].search([('id', '=', active_ids)])

        # student_id.education_ids.total_marks = student_id.education_ids.total_marks + self.grace_marks
        for rec in education_id:
            if rec:
                tot_marks = rec.total_marks + self.grace_marks
                rec.total_marks = float(tot_marks)
                # rec.write({'total_marks': tot_marks})
                # print(rec.total_marks)

    # @api.model
    # def default_get(self, fields_list):
    #     rec = super(GraceWizard, self).default_get(fields_list)
    #     active_ids = self._context.get('active_ids') or self._context.get('active_id')
    #
    #     print(active_ids)
    #
    #     student_id = self.env['students.details'].search([('id', '=', active_ids)])
    #
    #
    #     if active_ids:
    #         student_id.education_ids.total_marks = student_id.education_ids.total_marks + self.grace_marks
    #     # rec.update({
    #     #     'student_total'
    #     # })
    #     return rec
