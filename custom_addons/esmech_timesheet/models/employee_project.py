from odoo import fields, models


# FIXME: Create View for class Project
# Get back to the master class Employee Timesheet add m2o after completion

class EmployeeProject(models.Model):
    _name = 'employee.project'
    _description = 'Project'
    _rec_name = 'project_id'

    task_master_ids = fields.One2many('project.task.master', 'employee_proj_ids', "Task Master")
    sub_task_ids = fields.One2many('project.sub.task', 'employee_proj_ids', "Sub Task")
    project_id = fields.Char("Project No")
    customer_ref = fields.Char("Customer")
    description = fields.Char("Description")
    division = fields.Char("Division", readonly=True)
    drawing_no = fields.Text("Drawing No", readonly=True)
    search_key = fields.Text("Searchkey", readonly=True)

    #Don't know usage of below fields
    #Below Fields are buttons
    # projectstatus = fields.Text("Project Status")
    # em_esmts_import = fields.Text("Import Tasks")
    # allocatealert = fields.Text("Generate Task Alert")
    # synchronise = fields.Text("Synch ")
    # copytask = fields.Text("Copy Task")
    # customer = fields.Text("Create SubTask")


class TaskMaster(models.Model):
    _name = 'project.task.master'
    _description = 'Task Master'

    employee_proj_ids = fields.Many2one('employee.project')
    line = fields.Integer("Line")
    project_id = fields.Char("Project")
    task_name = fields.Char("Task Name")
    drawing_no = fields.Char("Drawing No", readonly=True)
    master_product = fields.Char("Master Product", readonly=True)
    assembly = fields.Char("Assembly", readonly=True)
    level_info = fields.Char("Level Info", readonly=True)
    billing_type = fields.Selection([
        ('billable', 'Billable'),
        ('non_billable', 'Non-Billable'),
        ('months', 'Months'),
    ], string='Billing Type')
    estimatehours_design = fields.Char("Estimated Hours (Design)")
    startdate_design = fields.Date("Start Date Design")
    deadline_design = fields.Date("Deadline (Design)")
    actualdeadline_dsgn = fields.Char("Actual DeadLine Design", readonly=True)
    spenttime_design = fields.Integer("Spent Time (Design)")
    variation_design = fields.Char("Variation (Design)", readonly=True)
    lasttrackingdate_design = fields.Date("Last Tracking Date (Design)")
    estimatehours_assembly = fields.Integer("Estimation Hours (Assembly)")
    deadline_assembly = fields.Date("Deadline (Assembly)")
    spenttime_assembly = fields.Integer("Spent Time (Assembly)")
    variation_assembly = fields.Char("Variation For (Assembly)", readonly=True)
    estimate_hours = fields.Integer("Total Estimated Hours")
    deadline = fields.Date("Deadline", readonly=True)
    spent_time = fields.Integer("Total Spent Time")
    variation = fields.Char("Total Variation", readonly=True)


class ProjectSubTask(models.Model):
    _name = 'project.sub.task'
    _description = 'Sub Task'

    employee_proj_ids = fields.Many2one('employee.project')
    is_active = fields.Boolean("Active")
    project_id = fields.Many2one('employee.project', "Project Name")
    task_name = fields.Char("Taskname", required=True)
    spent_time = fields.Char("Spent Time", readonly=True)
    master_product = fields.Char("Masterproduct")
    assembly = fields.Char("Assembly")
    line = fields.Char("Line")
    drawing_no = fields.Char("Drawingno")
    estimatehours_design = fields.Char("Estimated Hours(Design)")
    variation_design = fields.Char("Variation")



class ProjectEmployeeTask(models.Model) :
    _name = 'project.employee.task'
    _description = 'Employee Task'

    is_active = fields.Char("Active")
    employee_id = fields.Char("Employee Name")


class ProjectYearWiseSpend(models.Model):
    _name = 'project.yearwise.spend'
    _description = 'Yearwise Spend Hrs'

    project_id = fields.Char("Project")
    to_date = fields.Char("To Date")
    employee_department_id = fields.Char("Department") #many2one will get from employee class
    hours = fields.Float("Hours")
    remark = fields.Text("Remark")


