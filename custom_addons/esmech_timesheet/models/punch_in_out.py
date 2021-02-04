from odoo import fields, models


class PunchDetails(models.Model):
    """ Model for Main task creation """

    _name = 'punch.details'
    _description = 'Maintenance Stage'

    attendence_ids = fields.One2many('attendance.details', 'punch_id', "attendance id")
    organization = fields.Char("Organization")
    employee_id = fields.Char("Employee ID")
    employee = fields.Many2one("hr.employee.master", "Employee")
    punch_date = fields.Date("Punch Date")
    punch_in_time = fields.Float("Punch In Time (HH:MM:SS)")
    punch_out_time = fields.Float("Punch Out Time (HH:MM:SS)")
    shift_hours = fields.Float("Shift Hours (HH:MM:SS)")
    hours_worked = fields.Float("Hours Worked (HH:MM:SS)")
    reason = fields.Text("Reason")
    manual = fields.Boolean("Manual")
    attendance_status = fields.Many2one('attendance.status', 'Attendance Status')
    # attendance_status = fields.Selection([
    #     ('Absent', "Absent"),
    #     ('Comp off', "Comp off"),
    #     ('Half day', "Half day"),
    #     ('Holiday', "Holiday"),
    #     ('Leave', "Leave"),
    #     ('Loss of pay', "Loss of pay"),
    #     ('Maternity leave', "Maternity leave"),
    #     ('On tour', "On tour"),
    #     ('Overtime hour', "Overtime hour"),
    #     ('Present', "Present"),
    #     ('Weekend', "Weekend"),
    #     ('Worked On Weekend', "Worked On Weekend"),
    # ], string="Attendance Status")

    leave_type = fields.Many2one('leave.type', 'Leave Type')
    # leave_type = fields.Selection([
    #     ('Casual Leave', "Casual Leave"),
    #     ('Comp off', "Comp off"),
    #     ('Leave without pay', "Leave without pay"),
    #     ('Other leave', "Other leave"),
    #     ('Priviledged leave', "Priviledged leave"),
    #     ('short leave', "short leave"),
    #     ('sick leave', "sick leave"),
    # ], string="Leave Type")

    leave_status = fields.Selection([
        ('Approved', "Approved"),
        ('Draft', "Draft"),
        ('Pending', "Pending"),
        ('Rejected', "Rejected"),
    ], string="Leave Status")


class AttendanceDetails(models.Model):
    _name = 'attendance.details'
    _description = 'Attendence details of employees'

    punch_id = fields.Many2one('punch.details', "punch id")
    active = fields.Boolean("Active")
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
