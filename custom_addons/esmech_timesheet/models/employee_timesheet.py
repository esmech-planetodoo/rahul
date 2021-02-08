from odoo import fields, models


class EmployeeTimesheet(models.Model):
    _name = 'employee.timesheet'
    _description = 'Timesheet'

    timesheet_line_ids = fields.One2many('timesheet.line', 'employee_timesheet_id', "Timesheet Line")
    timesheet_history_ids = fields.One2many('timesheet.history', 'employee_timesheet_id', "Timesheet Line")
    org_id = fields.Char("Organization")
    employee_id = fields.Char("Employee")
    week_id = fields.Many2one('timesheet.week', 'Week')
    manager_id = fields.Many2one('hr.employee.master', "Manager")
    sun_working_hrs = fields.Float("Sunday (AH/WH)")
    mon_working_hrs = fields.Float("Monday (AH/WH)")
    tue_working_hrs = fields.Float("Tuesday (AH/WH)")
    wed_working_hrs = fields.Float("Wednesday (AH/WH)")
    thu_working_hrs = fields.Float("Thursday (AH/WH)")
    fri_working_hrs = fields.Float("Friday (AH/WH)")
    sat_working_hrs = fields.Float("Saturday (AH/WH)")
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
    insert_task = fields.Char("InsertTask")
    is_disapprove = fields.Boolean("Disapprove")
    # status = fields.Char("Status")
    # week_absent = fields.Boolean("Week Absent")
    insert_subtask = fields.Char("Insert-SubTask")
    send_approval = fields.Boolean("Send For Approve")


# FIXME: fix field type after completion of remaining master class
# every field is char field
# rename variable name
class TimesheetLine(models.Model):
    _name = 'timesheet.line'
    _description = 'Timesheet Line'

    employee_timesheet_id = fields.Many2one('employee.timesheet')
    project_name = fields.Char("Project Name")
    line_no = fields.Integer("Line No")
    task_id = fields.Char("Task")
    sub_task_id = fields.Char("Sub Task")
    monday = fields.Float("Monday")
    monday_desc = fields.Text("Monday Description")
    tuesday = fields.Float("Tuesday")
    tuesday_desc = fields.Text("Tuesday Description")
    wednesday = fields.Float("Wednesday")
    wednesday_desc = fields.Text("Wednesday Description")
    thursday = fields.Float("Thursday")
    thursday_desc = fields.Text("Thursday Description")
    friday = fields.Float("Friday")
    friday_desc = fields.Text("Friday Description")
    saturday = fields.Float("Saturday")
    saturday_desc = fields.Text("Saturday Description")
    sunday = fields.Float("Sunday")
    sunday_desc = fields.Text("Sunday Description")
    total = fields.Float("Total")
    drawing_no = fields.Char("Drawing No")
    description = fields.Char("Description")
    master_product = fields.Char("Master Product")

    # FIXME: Its an approval history fields have to figure out audit log for it

    # send_for_approval_date = fields.Char("Send For Approval Date")
    # doc_status = fields.Char("Document Status")
    # approval_to = fields.Char("Send for approval to")
    # approval_by = fields.Char("Send for approval by")
    # approved_by = fields.Char("Approved by")


class TimesheetHistory(models.Model):
    _name = 'timesheet.history'
    _description = 'Timesheet Line'

    employee_timesheet_id = fields.Many2one('employee.timesheet')
    remark = fields.Char("Remark")
    project_name = fields.Char("Project Name")
    name = fields.Char("Task Name")
    monday = fields.Char("Monday")
    tuesday = fields.Char("Tuesday")
    wednesday = fields.Char("Wednesday")
    thursday = fields.Char("Thursday")
    friday = fields.Char("Friday")
    saturday = fields.Char("Saturday")
    sunday = fields.Char("Sunday")
    description = fields.Char("Description")

    # cwts_timesheet_id = fields.Char("Time Sheet")


class TimesheetWeek(models.Model):
    _name = 'timesheet.week'
    _description = 'Timesheet Week'

    year_ids = fields.One2many('timesheet.year', 'week_id', "Timesheet Year")
    year = fields.Char("Fiscal Year")
    is_active = fields.Char("Active")
    create_week_master = fields.Char("Create Week Master")



class TimesheetYear(models.Model):
    _name = 'timesheet.year'
    _description = 'Timesheet Year'

    week_id = fields.Many2one('timesheet.week')
    enable = fields.Char("Enable")
    date_start = fields.Char("Start Date")
    week_no = fields.Char("Week No")
    description = fields.Char("Description")
    is_active = fields.Char("Active")
    date_end = fields.Char("End Date")
    year_master_id = fields.Char("Year")
