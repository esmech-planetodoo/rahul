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


class ImportDrawing(models.TransientModel):
    _inherit = 'import.process.plan'

    def import_drawing(self):
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
                    drawing_ob_id = value[0].strip() or False
                    ad_org_id = value[2].strip() or False
                    is_active = value[3] or False
                    created_by = value[5] or False
                    write_by = value[7] or False
                    update_date = value[6] or False
                    creation_date = value[4] or False
                    project_number_id = value[8].strip() or False
                    drawing_number = value[9].strip() or False
                    slash_number = value[10].strip() or False
                    mark_number = value[11].strip() or False
                    revision_number = value[12].strip() or False
                    revision_note = value[13].strip() or False
                    current_revision = value[14].strip() or False
                    description = value[15] or False
                    document_status = value[16] or False
                    create_revision = value[17].strip() or False
                    is_revised = value[18] or False
                    drawing_info = value[20] or False
                    is_process_entry = value[22].strip() or False
                    sms_drawing_number = value[24] or False
                    dt_cr = False
                    dt_wr = False
                    rev_date = False
                    if creation_date:
                        dt_cr = datetime.datetime.strptime(creation_date.split('.')[0], '%Y-%m-%d %H:%M:%S').strftime(
                            '%Y-%m-%d %H:%M:%S')
                    if update_date:
                        dt_wr = datetime.datetime.strptime(update_date.split('.')[0], '%Y-%m-%d %H:%M:%S').strftime(
                            '%Y-%m-%d %H:%M:%S')
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
                        'drawing_ob_id': drawing_ob_id,
                        'ad_org_id': org_id.id if org_id else False,
                        'is_active': is_active,
                        'creation_date': dt_cr,
                        'created_by': c_id.id if c_id else False,
                        'write_by': w_id.id if w_id else False,
                        'update_date': dt_wr,
                        # 'project_number_id': project_number_id,
                        'drawing_number': drawing_number,
                        'slash_number': slash_number,
                        'mark_number': mark_number,
                        'revision_number': revision_number,
                        'revision_note': revision_note,
                        'current_revision': current_revision,
                        'description': description,
                        'document_status': document_status,
                        'create_revision': create_revision,
                        'is_revised': is_revised,
                        'drawing_info': drawing_info,
                        'is_process_entry': is_process_entry,
                        'sms_drawing_number': sms_drawing_number
                    }
                    print("current revision>>>>>",current_revision )
                    if vals:
                        supplier_id = self.env['drawing.master'].create(vals)

            except Exception as e:
                _logger.error('------------Error Exception---------- %s', e, value[0])
                error_list.append(value)
        return error_list