from odoo import fields, models, api, _



class LoggerImport(models.Model):
    _name = 'logger.import'

    import_class = fields.Selection([
        ('user', 'User'),
        ('short_desc', 'Short Description'),
           ], string='Migrate Master Data')

    import_table_ids = fields.One2many('logger.import.line', 'table_id', string='Import Table')
    failed_record_ids = fields.One2many('failed.record.line','failed_id', string='Failed Record')

class LogerImportLine(models.Model):
    _name = 'logger.import.line'

    table_id = fields.Many2one('logger.import', string="Comodel Table")
    imported_table = fields.Char('Imported Table')
    start_time = fields.Date('Start Time')
    end_time = fields.Datetime('End Time')
    no_of_record_imported = fields.Char('No. Of Record Imported')
    no_of_record_failed = fields.Char('No. Of Record Failed To Import')



class FailedRecordLine(models.Model):
    _name = 'failed.record.line'

    failed_id = fields.Many2one('logger.import', string='Failed Id')
    failed_record = fields.Char('Failed Record')
    error_description = fields.Char('Error Description')


