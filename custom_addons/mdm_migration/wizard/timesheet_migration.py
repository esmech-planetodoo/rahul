import base64
import csv
from odoo import api, fields, models, _
import re
from odoo import exceptions, http
from tempfile import TemporaryFile
from odoo.exceptions import UserError
import io
import urllib.request as req
import logging
import datetime

_logger = logging.getLogger(__name__)


class TimesheetMigration(models.TransientModel):
    _name = 'timesheet.migration'
    _description = 'timesheet'

    upload_file = fields.Binary(string="File URL")

    def import_timesheet(self):
        print('inside def')
        csv_data = self.upload_file
        fileobj = TemporaryFile('wb+')
        csv_data = base64.decodebytes(csv_data)
        fileobj.write(csv_data)
        fileobj.seek(0)
        str_csv_data = fileobj.read().decode('utf-8')
        lis = csv.reader(io.StringIO(str_csv_data), delimiter=',')
        row_num = 0
        DATE_FORMAT = '%m/%d/%Y'
        error_list = []
        header_list = []
        data_dict = {}
        for row in lis:
            data_dict.update({row_num: row})
            row.append(row_num)
            row_num += 1
        for key, value in data_dict.items():
            try:
                if key == 0:
                    header_list.append(value)
                else:
                    _logger.info('-----row number----------- %s', key)
                    organization_id = value[0].strip() or False
                    is_active = value[2].strip() or False
                    description = value[9].strip() or False
                    values = value[7].strip() or False
                    name = value[8].strip() or False
                    is_summary = value[10] or False
                    is_allowed_period_control = value[12] or False
                    # date_cal = False
                    # print(datetime.datetime.strptime(calender_id.split('.')[0], '%Y-%m-%d %H:%M:%S'))
                    # if calender_id:
                    #     date_cal = datetime.datetime.strptime(calender_id.split('.')[0], '%Y-%m-%d %H:%M:%S').strftime(
                    #         '%Y-%m-%d %H:%M:%S')

                    vals = {
                        'name': name,
                        'is_active': is_active,
                        'description': description,
                        'is_summary': is_summary,
                        'organization_id': organization_id,
                        'is_allowed_period_control': is_allowed_period_control,

                    }
                    if vals:
                        print("in vals", vals)
                        timesheet_id = self.env['organization.master'].create(vals)

            except Exception as e:
                _logger.error('------------Error Exception---------- %s', e, value[1])
                error_list.append(value)
        return error_list

