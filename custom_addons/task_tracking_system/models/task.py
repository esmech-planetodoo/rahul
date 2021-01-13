from datetime import date, datetime, timedelta

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT

class TaskInfo(models.Model):
    """ Model for Main task creation """

    _name = 'task.info'
    _description = 'Maintenance Stage'

    name = fields.Char("Title")
    description = fields.Char("Description")
    task_create_date = fields.Date("Creation Date")
    task_assign_date = fields.Date("Assign Date")
