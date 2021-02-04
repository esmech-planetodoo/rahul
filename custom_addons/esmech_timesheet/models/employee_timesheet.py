from odoo import fields, models


class EmployeeTimesheet(models.Model):
    _name = 'employee.timesheet'
    _description = 'Timesheet'

    org_id = fields.Char("Organization")
    employee_id = fields.Char("Employee")
    weekmaster_id = fields.Many2one('timesheet.week')
    emp_mang_id = fields.Many2one('hr.employee.master', "Manager")
    sun_tot_working_hrs = fields.Float("Sunday (AH/WH)")
    mon_tot_working_hrs = fields.Float("Monday (AH/WH)")
    tue_tot_working_hrs = fields.Float("Tuesday (AH/WH)")
    wed_tot_working_hrs = fields.Float("Wednesday (AH/WH)")
    thu_tot_working_hrs = fields.Float("Thursday (AH/WH)")
    fri_tot_working_hrs = fields.Float("Friday (AH/WH)")
    sat_tot_working_hrs = fields.Float("Saturday (AH/WH)")
    sun_ontour = fields.Boolean("Sunday On Tour")
    mon_ontour = fields.Boolean("Monday On Tour")
    tue_ontour = fields.Boolean("Tuesday On Tour")
    wed_ontour = fields.Boolean("Wednesday On Tour")
    thu_ontour = fields.Boolean("Thursday On Tour")
    fri_ontour = fields.Boolean("Friday On Tour")
    sat_ontour = fields.Boolean("Saturday On Tour")
    description = fields.Text("Description")

    # Rest below fields still to figure out
    copy_last_week_task = fields.Char("Copy Last Week Task")
    inserttask_asmby = fields.Char("InsertTask")
    reject = fields.Boolean("Disapprove")
    status = fields.Char("Status")
    week_absent = fields.Boolean("Week Absent")
    inserttask = fields.Char("Insert-SubTask")
    taskwise_approval_process = fields.Boolean("Send For Approve")


# FIXME: fix field type after completion of remaining master class
# every field is char field
# rename variable name
class TimesheetLine(models.Model):
    _name = 'timesheet.line'
    _description = 'Timesheet Line'

    project_id = fields.Char("Project Name")
    line = fields.Integer("Line No")
    saturday_desc = fields.Char("Saturday Description")
    wednesday_desc = fields.Char("Wednesday Description")
    sunday_desc = fields.Char("Sunday Description")
    friday_desc = fields.Char("Friday Description")
    monday_desc = fields.Char("Monday Description")
    thursday_desc = fields.Char("Thursday Description")
    tuesday_desc = fields.Char("Tuesday Description")
    total = fields.Char("Total")
    wednesday = fields.Char("Wednesday")
    saturday = fields.Char("Saturday")
    tuesday = fields.Char("Tuesday")
    thursday = fields.Char("Thursday")
    send_for_approval_date = fields.Char("Send For Approval Date")
    drawingno = fields.Char("Drawing No")
    docstatus = fields.Char("Document Status")
    approval_to = fields.Char("Send for approval to")
    approval_by = fields.Char("Send for approval by")
    sunday = fields.Char("Sunday")
    cwts_sub_task_id = fields.Char("Sub Task")
    masterproduct = fields.Char("Master Product")
    monday = fields.Char("Monday")
    description = fields.Char("Description")
    approved_by = fields.Char("Approved by")
    cwts_task_master_id = fields.Char("Task")
    friday = fields.Char("Friday")


class TimesheetHistory(models.Model):
    _name = 'timesheet.history'
    _description = 'Timesheet Line'

    friday = fields.Char("Friday")
    sunday = fields.Char("Sunday")
    tuesday = fields.Char("Tuesday")
    saturday = fields.Char("Saturday")
    thursday = fields.Char("Thursday")
    remark = fields.Char("Remark")
    cwts_project_id = fields.Char("Project Name")
    wednesday = fields.Char("Wednesday")
    monday = fields.Char("Monday")
    cwts_timesheet_id = fields.Char("Time Sheet")
    description = fields.Char("Description")
    name = fields.Char("Task Name")


class TimesheetWeek(models.Model):
    _name = 'timesheet.week'
    _description = 'Timesheet Week'

    year_ids = fields.One2many('timesheet.year', 'week_id', "Year Master")
    createweekmaster = fields.Char("Create Week Master")
    year = fields.Char("Fiscal Year")
    isactive = fields.Char("Active")


class TimesheetYear(models.Model):
    _name = 'timesheet.year'
    _description = 'Timesheet Year'

    week_id = fields.Many2one('timesheet.week')
    enable = fields.Char("Enable")
    datestart = fields.Char("Start Date")
    weekno = fields.Char("Week No")
    description = fields.Char("Description")
    isactive = fields.Char("Active")
    date_end = fields.Char("End Date")
    cwts_yearmaster_id = fields.Char("Year")
