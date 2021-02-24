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


class ImportMOC(models.TransientModel):
    _inherit = 'import.process.plan'

    def import_moc(self):
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
                    moc_ob_id = value[0].strip() or False
                    ad_org_id = value[2].strip() or False
                    is_active = value[3] or False
                    created_by = value[5] or False
                    write_by = value[7] or False
                    update_date = value[6] or False
                    creation_date = value[4] or False
                    inst = value[8].strip() or False
                    bs = value[9].strip() or False
                    din = value[10].strip() or False
                    jis = value[11].strip() or False
                    remark = value[12].strip() or False
                    name = value[13].strip() or False
                    application = value[14].strip() or False
                    send_for_approval_by_id = value[15] or False
                    approved_By = value[16] or False
                    document_Status = value[17].strip() or False
                    send_for_approval_to_id = value[18] or False
                    create_revision = value[21] or False
                    revision_no = value[22].strip() or False
                    revision_date = value[23] or False
                    revision_remark = value[24].strip() or False
                    current_revision = value[25].strip() or False
                    rev_prepared_by = value[26] or False
                    dt_cr = False
                    dt_wr = False
                    rev_date = False
                    if creation_date:
                        dt_cr = datetime.datetime.strptime(creation_date.split('.')[0], '%Y-%m-%d %H:%M:%S').strftime(
                            '%Y-%m-%d %H:%M:%S')
                    if update_date:
                        dt_wr = datetime.datetime.strptime(update_date.split('.')[0], '%Y-%m-%d %H:%M:%S').strftime(
                            '%Y-%m-%d %H:%M:%S')
                    if revision_date:
                        rev_date = datetime.datetime.strptime(revision_date.split('.')[0], '%Y-%m-%d %H:%M:%S').strftime(
                            '%Y-%m-%d %H:%M:%S')
                        print("rev_date>>>>>", rev_date)
                    org_id = []
                    c_id = []
                    w_id = []
                    send_for_app_id = []
                    app_by_id = []
                    send_to_id = []
                    rev_prep_id = []
                    if ad_org_id:
                        org_id = self.env['esmech.organization'].search(
                            [('ob_id', '=', ad_org_id)])
                    if created_by:
                        c_id = self.env['res.users'].search(
                            [('user_ob_id', '=', created_by)])
                    if write_by:
                        w_id = self.env['res.users'].search(
                            [('user_ob_id', '=', write_by)])
                    if send_for_approval_by_id:
                        send_for_app_id = self.env['res.users'].search(
                            [('user_ob_id', '=', send_for_approval_by_id)])
                    if approved_By:
                        app_by_id = self.env['res.users'].search(
                            [('user_ob_id', '=', approved_By)])
                    if send_for_approval_to_id:
                        send_to_id = self.env['res.users'].search(
                            [('user_ob_id', '=', send_for_approval_to_id)])
                    if rev_prepared_by:
                        rev_prep_id = self.env['res.users'].search(
                            [('user_ob_id', '=', rev_prepared_by)])
                    vals = {
                        'moc_ob_id': moc_ob_id,
                        'ad_org_id': org_id.id if org_id else False,
                        'is_active': is_active,
                        'creation_date': dt_cr,
                        'created_by': c_id.id if c_id else False,
                        'write_by': w_id.id if w_id else False,
                        'update_date': dt_wr,
                        'inst': inst,
                        'bs': bs,
                        'din': din,
                        'jis': jis,
                        'remark': remark,
                        'name': name,
                        'application': application,
                        'send_for_approval_by_id': send_for_app_id.id if send_for_app_id else False,
                        'approved_By': app_by_id.id if app_by_id else False,
                        'document_Status': document_Status,
                        'create_revision': create_revision,
                        'send_for_approval_to_id': send_to_id.id if send_to_id else False,
                        'revision_no': revision_no,
                        'revision_date': rev_date,
                        'revision_remark': revision_remark,
                        'current_revision': current_revision,
                        'rev_prepared_by': rev_prep_id.id if rev_prep_id else False,
                    }
                    print("name>>>>>", )
                    if vals:
                        supplier_id = self.env['mat.construction'].create(vals)

            except Exception as e:
                _logger.error('------------Error Exception---------- %s', e, value[0])
                error_list.append(value)
        return error_list
