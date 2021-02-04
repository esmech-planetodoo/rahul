from odoo import fields, models


# FIXME: Add proper field type
# arrange in proper order
# Get back to the master class Employee Timesheet add m2o after completion

class EmployeeProject(models.Model):
    _name = 'employee.project'
    _description = 'Project'

    description = fields.Text("Description")
    division = fields.Text("Division")
    drawingno = fields.Text("Drawing No")
    projectstatus = fields.Text("Project Status")
    em_esmts_import = fields.Text("Import Tasks")
    allocatealert = fields.Text("Generate Task Alert")
    c_project_id = fields.Text("Project No")
    synchronise = fields.Text("Synch ")
    searchkey = fields.Text("Searchkey")
    copytask = fields.Text("Copy Task")
    Customer = fields.Text("Create SubTask")


class TaskMaster(models.Model):
    _name = 'project.task.master'
    _description = 'Task Master'

    deadline_design = fields.Char("Deadline (Design)")
    variation_design = fields.Char("Variation (Design)")
    actualdeadline_dsgn = fields.Char("Actual DeadLine Design")
    spenttime = fields.Char("Total Spent Time")
    levelinfo = fields.Char("Level Info")
    spenttime_assembly = fields.Char("Spent Time (Assembly)")
    cwts_project_id = fields.Char("Project")
    drawingno = fields.Char("Drawing No")
    estimatehours = fields.Char("Total Estimated Hours")
    billingtype = fields.Char("Billing Type")
    line = fields.Char("Line")
    deadline_assembly = fields.Char("Deadline (Assembly)")
    taskname = fields.Char("Task Name")
    masterproduct = fields.Char("Master Product")
    spenttime_design = fields.Char("Spent Time (Design)")
    estimatehours_assembly = fields.Char("Estimation Hours (Assembly)")
    deadline = fields.Char("Deadline")
    startdate_design = fields.Char("Start Date Design")
    assembly = fields.Char("Assembly")
    lasttrackingdate_design = fields.Char("Last Tracking Date (Design)")
    variation = fields.Char("Total Variation")
    variation_assembly = fields.Char("Variation For (Assembly)")
    estimatehours_design = fields.Char("Estimated Hours (Design)")


class ProjectSubTask(models.Model):
    _name = 'project.sub.task'
    _description = 'Sub Task'

    taskname = fields.Char("Taskname")
    line = fields.Char("Line")
    masterproduct = fields.Char("Masterproduct")
    cwts_project_id = fields.Char("Project Name")
    estimatehours_design = fields.Char("Estimated Hours(Design)")
    isactive = fields.Char("Active")
    variation_design = fields.Char("Variation")
    drawingno = fields.Char("Drawingno")
    assembly = fields.Char("Assembly")
    spenttime = fields.Char("Spent Time")


class ProjectEmployeeTask(models.Model) :
    _name = 'project.employee.task'
    _description = 'Employee Task'

    isactive = fields.Char("Active")
    exdhrm_employee_id = fields.Char("Employee Name")


class ProjectYearWiseSpend(models.Model):
    _name = 'project.yearwise.spend'
    _description = 'Yearwise Spend Hrs'

    cwts_project_id = fields.Char("Project")
    exdhrm_employee_department_id = fields.Char("Department")
    hours = fields.Char("Hours")
    todate = fields.Char("To Date")
    remark = fields.Char("Remark")
