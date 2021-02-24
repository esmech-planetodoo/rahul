from odoo import api, fields, models, _
import re
from odoo import exceptions, http
from tempfile import TemporaryFile
from odoo.exceptions import UserError
import io
import urllib.request as req
import logging
# from esmech_erp.mdm_migration.wizard.department_wizard import ImportDepartment
from .department_wizard import ImportDepartment
from .process_plan_wizard import ImportProcessPlan
from .moc_wizard import ImportMOC
from .drawing_wizard import ImportDrawing
from .timesheet_migration import TimesheetMigration
import datetime

_logger = logging.getLogger(__name__)


class ImportMaster(models.TransientModel):
    _name = 'import.master'
    import_class = fields.Selection([
        ('user', 'User'),
        ('short_desc', 'Short Description'),
        ('department', 'Department'),
        ('process_plan', 'Process Plan'),
        ('update_doc_in_process_plan', 'Update Document No In Process Plan'),
        ('process_plan_activity', 'Process Plan Import  Activity'),
        ('import_operation', 'Process Plan Import Operation'),
        ('import_process_plan', 'Process Plan Available'),
        ('moc', 'MOC'),
        ('drawing', 'Drawing Master'),
        ('timesheet', 'Timesheet'),
        ('designation', 'Designation'),
        ('product', 'Product'),
    ], string='Migrate Master Data')
    upload_file = fields.Binary(string='File URL')

    def import_master(self):
        if self.import_class == 'department':
            errors = ImportDepartment.import_department(self)
        if self.import_class == 'process_plan':
            pro_errors = ImportProcessPlan.import_process_plan(self)
        if self.import_class == 'update_doc_in_process_plan':
            update_process = ImportProcessPlan.update_process_document(self)
        if self.import_class == 'moc':
            import_moc = ImportMOC.import_moc(self)
        if self.import_class == 'drawing':
            import_moc = ImportDrawing.import_drawing(self)
        if self.import_class == 'process_plan_activity':
            import_moc = ImportProcessPlan.import_activity(self)
        if self.import_class == 'process_plan_activity':
            import_moc = ImportProcessPlan.import_activity(self)
        if self.import_class == 'import_operation':
            import_moc = ImportProcessPlan.import_operation(self)
        if self.import_class == 'import_process_plan':
            import_moc = ImportProcessPlan.check_process_plane(self)
        if self.import_class == 'timesheet':
            import_timesheet = TimesheetMigration.import_timesheet(self)
        if self.import_class == 'designation':
            import_designation = TimesheetMigration.import_designation(self)
        return
