from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


class EmployeeRecord(models.Model):
    """ Model for Master employee record """

    _name = 'employee.record'
    _description = 'Maintenance Employee details'

    employee_id = fields.Char("Employee Id")
    card_no = fields.Char("Card No")
    first_name = fields.Char("First Name")
    middle_name = fields.Char("Middle Name")
    last_name = fields.Char("Last Name")
    email = fields.Char("Email")
    alter_email = fields.Char("Alternate Email")
    phone_no = fields.Char("Phone No.")
    mobile_no = fields.Char("Mobile No.")
    alter_phone = fields.Char("Alternate Phone No.")
    emergency_contact = fields.Char("Emergency Contact No.")
    image = fields.Binary("Image")
    description = fields.Char("Description")
    active = fields.Char("Active")
    shift = fields.Char("Shift")
    rotation = fields.Char("Rotation")
    business_partner = fields.Char("Business Partner")
    user_contact = fields.Char("User/Contact")
    add_data = fields.Char("ADD Data")


class PersonalInformation(models.Model):
    """ Model for Child personal information """

    _name = 'employee.record'
    _description = 'Personal Information'

    employee = fields.Char("Employee")
    father_name = fields.Char("Father Name")
    mother_name = fields.Char("Mother Name")
    nick_name = fields.Char("Nick Name")
    spouse_name = fields.Char("Spouse Name")
    gender = fields.Selection([
        ("male", "male"),
        ("female", "female"),
    ], string="Gender")
    marital_status = fields.Char("Marital Status")
    birthday = fields.Char("Birthday")
    age = fields.Char("Age")
    place_birth = fields.Char("Place of Birth")
    blood_group = fields.Char("Blood Group")
    religion = fields.Char("Religion")
    dependent_no = fields.Char("No. of Dependents")
    citizenship = fields.Char("Citizenship")
    ethnic_race = fields.Char("Ethnic Race")
    pf_no = fields.Char("PF/EPF No.")
    active = fields.Char("Active")
    driving_lic = fields.Char("Driving License No.")
    dl_issue_date = fields.Char("Driving License Issue Date")
    dl_expiry_date = fields.Char("Driving License Expiry Date")
    pan_no = fields.Char("PAN No.")
    passport_no = fields.Char("Passport No.")
    passport_issue_date = fields.Char("Passport Issue Date")
    passport_expiry_date = fields.Char("Passport Expiry Date")
    esi_no = fields.Char("ESI No.")
    uid_no = fields.Char("Unique Identity Card No.")


class EmployeeLocation(models.Model):
    """ Model for Child location/address """

    _name = 'employee.location'
    _description = 'employee residential details'

    employee_name = fields.Char("Employee")
    address = fields.Char("Location / Address")
    present_address = fields.Char("Present")
    permanent_address = fields.Char("Permanent")
    default = fields.Char("Default")
    active = fields.Char("Active")
    location_type = fields.Char("Location Type")


class EmployeeJob(models.Model):
    """ Model for Child work details """

    _name = 'employee.job'
    _description = 'Employee work details'

    payment_method = fields.Char("Payment Method")
    employee = fields.Char("Employee")
    financial_acc = fields.Char("Financial Account")
    define_weekends = fields.Char("Define Weekends")
    work_shift = fields.Char("Work Shift")
    designation = fields.Char("Designation/Position")
    team = fields.Char("Team")
    pay_grade = fields.Char("Pay Grade")
    emp_category = fields.Char("Employee Category")
    emp_department = fields.Char("Employee Department")
    date_joining = fields.Char("Date of Joining")
    years_service = fields.Char("Years Of Service")
    probation_period = fields.Char("Probation Period")
    confirmation_date = fields.Char("Confirmation Date")
    retirement_date = fields.Char("Retirement Date")
    relieved_date = fields.Char("Relieved Date")
    reason_leaving = fields.Char("Reason for Leaving")
    leave_policy = fields.Char("Leave Policy")
    active = fields.Char("Active")


class EmployeeExperience(models.Model):
    """ Model for Child Work Experience Information """

    _name = 'employee.experience'
    _description = 'Employee Work Experience Information'

    employee_name = fields.Char("Employee")
    prev_employer = fields.Char("Previous Employer")
    designation = fields.Char("Designation")
    date_of_join = fields.Char("Date of Join")
    salary = fields.Char("Salary")
    relieved_date = fields.Char("Relieved Date")
    reason_for_relieving = fields.Char("Reason for Relieving")
    active = fields.Char("Active")


class EmployeeQualification(models.Model):
    """ Model for Child Educational qualification """

    _name = 'employee.qualification'
    _description = 'Employee Educational qualification'

    employee_name = fields.Char("Employee")
    degree = fields.Char("Degree")
    specialisation = fields.Char("Specialisation")
    institute = fields.Char("Institute")
    university = fields.Char("University")
    year_of_pass = fields.Char("Year of Passing")
    percentage = fields.Char("Percentage")


class EmployeeBankInfo(models.Model):
    """ Model for Child Educational qualification """

    _name = 'employee.bankinfo'
    _description = 'Employee Bank Account Details'

    employee_name = fields.Char("Employee")
    account_no = fields.Char("Account No.")
    account_name = fields.Char("Account Name")
    bank_name = fields.Char("Bank Name")
    branch_name = fields.Char("Branch Name")
    description = fields.Char("Description")
    default = fields.Char("Default")


class EmployeeLeaveInfo(models.Model):
    """ Model for Child Leave Information """

    _name = 'employee.Leaveinfo'
    _description = 'Employee Leave Information'

    employee_name = fields.Char("Employee")
    leave_type = fields.Char("Leave Type")
    available_leaves = fields.Char("Available Leaves")
    encashed_leaves = fields.Char("Encashed Leaves")
    leaves_taken = fields.Char("Leaves Taken")
    accured = fields.Char("Accrued For Month Year(MM-YYYY)")


class EmployeeLeaveDetails(models.Model):
    """ Model for Child Leave Details """

    _name = 'employee.Leavedetails'
    _description = 'Employee Leave Details'

    leave = fields.Char("Leave Date")
    reason = fields.Char("Reason")
    leave_requisition = fields.Char("Leave Requisition")
    employee_punch = fields.Char("Employee Punch")
    leave_status = fields.Char("Leave Status")
    accured_on = fields.Char("Accrued On")
    valid_till = fields.Char("Valid Till Date")
    avail_leaves = fields.Char("Available Leaves")


class EmployeeShift(models.Model):
    """ Model for Child Shift Details """

    _name = 'employee.shift'
    _description = 'Employee Shift Details'

    shift_schedule = fields.Char("Shift schedule")
    start_day = fields.Char("Start day")
    end_day = fields.Char("End day")
    rotation = fields.Char("Shift Rotation")
    employee_name = fields.Char("Employee")
    description = fields.Char("Description")
