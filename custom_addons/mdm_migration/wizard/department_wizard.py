
import base64
import csv
from odoo import api, fields, models,_
import re
from odoo import exceptions, http
from tempfile import TemporaryFile
from odoo.exceptions import UserError
import io
import urllib.request as req
import logging
import datetime


_logger = logging.getLogger(__name__)


class ImportDepartment(models.TransientModel):
    _name = 'import.department'

    upload_file = fields.Binary(string='File URL')


    def import_department(self):
        csv_datas = self.upload_file
        fileobj = TemporaryFile('wb+')
        csv_datas = base64.decodebytes(csv_datas)
        fileobj.write(csv_datas)
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
                    department_ob_id = value[0].strip() or False
                    ad_client_id = value[1].strip() or False
                    ad_org_id = value[2].strip() or False
                    is_active = value[3] or False
                    creation_date = value[4] or False
                    created_by = value[5] or False
                    update_date = value[6] or False
                    write_by = value[7] or False
                    values = value[8] or False
                    name = value[9].strip() or False
                    description = value[10].strip() or False
                    dt_cr = False
                    dt_wr = False
                    if creation_date:
                        dt_cr = datetime.datetime.strptime(creation_date.split('.')[0], '%Y-%m-%d %H:%M:%S').strftime(
                            '%Y-%m-%d %H:%M:%S')
                        print("date>>>>>", name, dt_cr)
                    if update_date:
                        dt_wr = datetime.datetime.strptime(update_date.split('.')[0], '%Y-%m-%d %H:%M:%S').strftime(
                            '%Y-%m-%d %H:%M:%S')
                        print("date>>>>>", name, dt_wr)
                    org_id = []
                    c_id = []
                    w_id = []
                    if ad_org_id:
                        org_id = self.env['esmech.organization'].search(
                            [('ob_id', '=', ad_org_id)])
                    if created_by:
                        c_id = self.env['res.users'].search(
                            [('user_ob_id', '=', created_by)])
                    if write_by:
                        w_id = self.env['res.users'].search(
                            [('user_ob_id', '=', write_by)])
                    vals = {
                        'department_ob_id': department_ob_id,
                        'ad_client_id': ad_client_id,
                        'ad_org_id': org_id.id if org_id else False,
                        'is_active': is_active,
                        'creation_date': creation_date,
                        'created_by': c_id.id if c_id else False,
                        'write_by': w_id.id if w_id else False,
                        'update_date': dt_wr,
                        'value': values,
                        'name': name,
                        'description': description,
                    }
                    print("name>>>>>", )
                    if vals:
                        supplier_id = self.env['extc.department'].create(vals)

            except Exception as e:
                _logger.error('------------Error Exception---------- %s', e, value[0])
                error_list.append(value)
        return error_list