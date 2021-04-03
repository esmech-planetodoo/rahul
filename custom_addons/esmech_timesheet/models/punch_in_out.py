from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import datetime
import re


class PunchDetails(models.Model):
    """ Model for Main task creation """

    _name = 'punch.details'
    _description = 'Maintenance Stage'
    _rec_name = 'employee'

    attendence_ids = fields.One2many('attendance.details', 'punch_id', "attendance id")
    organization = fields.Many2one('organization.master', "Organization")
    employee_id = fields.Char("Employee ID", readonly=True)
    employee = fields.Many2one("hr.employee.master", "Employee", required=True)
    punch_date = fields.Date("Punch Date", required=True, default=datetime.today())
    punch_in_time = fields.Float("Punch In Time (HH:MM)")
    punch_out_time = fields.Float("Punch Out Time (HH:MM)", default=0.0)
    shift_hours = fields.Float("Shift Hours (HH:MM)")
    hours_worked = fields.Float("Hours Worked (HH:MM)", compute='_compute_hours_worked')
    reason = fields.Text("Reason")
    manual = fields.Boolean("Manual")
    attendance_status = fields.Many2one('attendance.status', 'Attendance Status', required=True)
    leave_type = fields.Many2one('leave.type', 'Leave Type')

    leave_status = fields.Selection([
        ('Approved', "Approved"),
        ('Draft', "Draft"),
        ('Pending', "Pending"),
        ('Rejected', "Rejected"),
    ], string="Leave Status")

    @api.onchange('punch_in_time', 'punch_out_time')
    def _check_hours(self):
        if self.punch_in_time < 0:
            raise ValidationError(_('Time should be greater than 0'))
        elif self.punch_in_time > 23.99:
            raise ValidationError("Time should be below 24")
        elif self.punch_out_time < 0.0:
            raise ValidationError("time should be greater than 0")
        elif self.punch_out_time >= 23.59:
            raise ValidationError("Time should be below 24")

    @api.depends('punch_in_time', 'punch_out_time')
    def _compute_hours_worked(self):
        print(self.punch_in_time)
        for rec in self:
            print(rec.punch_in_time)
            total_hours = rec.punch_out_time - rec.punch_in_time
            if total_hours < 0:
                rec.hours_worked = 24 + total_hours
            else:
                rec.hours_worked = total_hours

    @api.model
    def create(self, vals):
        attendence_vals = {
            'employee_id': vals['employee_id'] if 'employee_id' in vals else self.employee_id,
            'punch_date': vals['punch_date'] if 'punch_date' in vals else self.punch_date,
            'punch_time': vals['punch_in_time'] if 'punch_in_time' in vals else self.punch_in_time,
        }
        vals['attendence_ids'] = [(0, 0, attendence_vals)]
        rec = super(PunchDetails, self).create(vals)
        return rec

    # override function to update values in many2one
    def write(self, vals):
        if 'punch_date' in vals or 'punch_in_time' in vals and 'employee_id' not in vals:
            attendence_vals = {
                'employee_id': vals['employee_id'] if 'employee_id' in vals else self.employee_id,
                'punch_date': vals['punch_date'] if 'punch_date' in vals else self.punch_date,
                'punch_time': vals['punch_in_time'] if 'punch_in_time' in vals else self.punch_in_time,
            }
            vals.update({'attendence_ids': [(0, 0, attendence_vals)]})
        rec = super(PunchDetails, self).write(vals)
        return rec

    @api.onchange('employee')
    def emp_id(self):
        emp_obj = self.env['hr.employee.master'].search([('id', '=', self.employee.id)])
        if emp_obj.employee_roll_no:
            self.employee_id = emp_obj.employee_roll_no
        else:
            self.employee_id = '0000'


class AttendanceDetails(models.Model):
    _name = 'attendance.details'
    _description = 'Attendence details of employees'

    punch_id = fields.Many2one('punch.details', "punch id")
    is_active = fields.Boolean("Active")
    punch_date = fields.Date("Punch Date")
    employee_id = fields.Char("Employee ID")
    punch_time = fields.Char("Punch Time")
    processed = fields.Char("Processed")

# class AttendanceLine(models.Model):
#     _name = 'attendance.line'
#     _description = 'Detail of '
#
#     active = fields.Boolean("Active")
#     punch_date = fields.Date("Punch Date")
#     employee_id = fields.Char("Employee ID")
#     punch_time = fields.Char("Punch Time")
#     processed = fields.Char("Processed")
