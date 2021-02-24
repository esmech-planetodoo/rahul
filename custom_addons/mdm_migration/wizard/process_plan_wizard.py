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


class ImportProcessPlan(models.TransientModel):
    _name = 'import.process.plan'

    upload_file = fields.Binary(string='File URL')

    def import_process_plan(self):
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
                    name = value[9].strip() or False
                    process_plan_ob_id = value[0].strip() or False
                    ad_org_id = value[2].strip() or False
                    active = value[3] or False
                    created_by = value[5] or False
                    write_by = value[7] or False
                    update_date = value[6] or False
                    creation_date = value[4] or False
                    values = value[8] or False
                    description = value[10].strip() or False
                    is_operation_insert = value[11] or False
                    process_unit = value[12].strip() or False
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
                        'name': name,
                        'process_plan_ob_id': process_plan_ob_id,
                        'ad_org_id': org_id.id if org_id else False,
                        'active': active,
                        'creation_date': dt_cr,
                        'created_by': c_id.id if c_id else False,
                        'write_by': w_id.id if w_id else False,
                        'update_date': dt_wr,
                        'description': description,
                        'is_operation_insert': is_operation_insert,
                        'process_unit': process_unit,
                        'value': values,
                    }
                    print("name>>>>>", )
                    if vals:
                        supplier_id = self.env['mrp.routing'].create(vals)

            except Exception as e:
                _logger.error('------------Error Exception---------- %s', e, value[1])
                error_list.append(value)
        return error_list

    def update_process_document(self):
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
                    process_plan_ob_id = value[0].strip() or False
                    document_no = value[1].strip() or False
                    date_from = value[2] or False
                    date_to = value[3] or False
                    dt_cr = False
                    dt_wr = False
                    if date_from:
                        dt_cr = datetime.datetime.strptime(date_from.split('.')[0], '%Y-%m-%d %H:%M:%S').strftime(
                            '%Y-%m-%d %H:%M:%S')
                        print("date>>>>>", dt_cr)
                    if date_to:
                        dt_wr = datetime.datetime.strptime(date_to.split('.')[0], '%Y-%m-%d %H:%M:%S').strftime(
                            '%Y-%m-%d %H:%M:%S')
                        print("date>>>>>", dt_wr)
                    doc_no = {1}
                    if document_no not in doc_no:
                        doc_no.add(document_no)
                        plan_id = self.env['mrp.routing'].search(
                            [('process_plan_ob_id', '=', process_plan_ob_id)])
                        vals = {
                            'document_no': document_no,
                            'starting_date': dt_cr,
                            'ending_date': dt_wr,
                        }
                        print("name>>>>>", )
                        if vals:
                            supplier_id = plan_id.write(vals)

            except Exception as e:
                _logger.error('------------Error Exception---------- %s', e, value[0])
                error_list.append(value)
        return error_list

    def import_activity(self):
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
                    activity_ob_id = value[0].strip() or False
                    ad_org_id = value[2].strip() or False
                    active = value[3] or False
                    created_by = value[5] or False
                    write_by = value[7] or False
                    update_date = value[6] or False
                    creation_date = value[4] or False
                    name = value[8] or False
                    values = value[9].strip() or False
                    note = value[11] or False
                    is_fabrication_process = value[13] or False
                    cost_centre_use_time = value[14] or False
                    preparation_time = value[15] or False
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
                        'activity_ob_id': activity_ob_id,
                        'ad_org_id': org_id.id if org_id else False,
                        'active': active,
                        'creation_date': dt_cr,
                        'created_by': c_id.id if c_id else False,
                        'write_by': w_id.id if w_id else False,
                        'update_date': dt_wr,
                        'name': name,
                        'code': values,
                        'note': note,
                        'is_fabrication_process': is_fabrication_process,
                        'cost_centre_use_time': cost_centre_use_time,
                        'preparation_time': preparation_time,
                    }
                    print("name>>>>>", )
                    if vals:
                        supplier_id = self.env['mrp.workcenter'].create(vals)

            except Exception as e:
                _logger.error('------------Error Exception---------- %s', e, value[1])
                error_list.append(value)
        return error_list

    def import_operation(self):
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
                    process_plan_ob_id = value[1] or False
                    activity_ob_id = value[40].strip() or False
                    document_no = value[18] or False
                    name = value[22].strip() or False
                    values = value[23].strip() or False
                    description = value[24].strip() or False
                    cost_centre_use_time = value[25] or False
                    preparation_time = value[26] or False
                    is_fabrication_process = value[38] or False
                    sequence = value[28] or False
                    estimated_time = value[36] or False
                    multiplier = value[27] or False
                    # values = value[9].strip() or False
                    # note = value[11] or False
                    # is_fabrication_process = value[13] or False
                    # cost_centre_use_time = value[14] or False
                    # preparation_time = value[15] or False
                    # dt_cr = False
                    # dt_wr = False
                    # if creation_date:
                    #     dt_cr = datetime.datetime.strptime(creation_date.split('.')[0], '%Y-%m-%d %H:%M:%S').strftime(
                    #         '%Y-%m-%d %H:%M:%S')
                    #     print("date>>>>>", name, dt_cr)
                    # if update_date:
                    #     dt_wr = datetime.datetime.strptime(update_date.split('.')[0], '%Y-%m-%d %H:%M:%S').strftime(
                    #         '%Y-%m-%d %H:%M:%S')
                    #     print("date>>>>>", name, dt_wr)
                    # org_id = []
                    # c_id = []
                    # w_id = []
                    activity_id = []
                    route_id = []
                    # if ad_org_id:
                    #     org_id = self.env['esmech.organization'].search(
                    #         [('ob_id', '=', ad_org_id)])
                    # if created_by:
                    #     c_id = self.env['res.users'].search(
                    #         [('user_ob_id', '=', created_by)])
                    # if write_by:
                    #     w_id = self.env['res.users'].search(
                    #         [('user_ob_id', '=', write_by)])
                    if process_plan_ob_id:
                        route_id = self.env['mrp.routing'].search(
                            [('process_plan_ob_id', '=', process_plan_ob_id)])
                        if route_id:
                            if activity_ob_id:
                                activity_id = self.env['mrp.workcenter'].search(
                                    [('activity_ob_id', '=', activity_ob_id)])
                                vals = {
                                    'routing_id': route_id.id,
                                    'name': name if name else False,
                                    'workcenter_id': activity_id.id if activity_id.id else False,
                                    'value': activity_id.code if activity_id.code else False,
                                    'cost_centre_use_time': activity_id.cost_centre_use_time if activity_id.cost_centre_use_time else False,
                                    'preparation_time': activity_id.preparation_time if activity_id.preparation_time else False,
                                    'description': activity_id.note if activity_id.note else False,
                                    'is_fabrication_process': activity_id.is_fabrication_process if activity_id.is_fabrication_process else False,
                                    'is_active': activity_id.active if activity_id.active else False,
                                    'sequence': sequence,
                                    'estimated_time': estimated_time,
                                    'multiplier': multiplier,
                                    # 'created_by': c_id.id if c_id else False,
                                    # 'write_by': w_id.id if w_id else False,
                                    # 'update_date': dt_wr,
                                    # 'name': name,
                                    # 'code': values,
                                    # 'note': note,
                                    # 'is_fabrication_process': is_fabrication_process,
                                    # 'cost_centre_use_time': cost_centre_use_time,
                                    # 'preparation_time': preparation_time,
                                }
                                print("vals>>>>>", vals)
                                if vals:
                                    process_id = self.env['mrp.routing'].search(
                                        [('document_no', '=', document_no)])
                                    process_id.operation_ids.create(vals)
            except Exception as e:
                _logger.error('------------Error Exception---------- %s', e, value[18])
                error_list.append(value)
        return error_list

    def check_process_plane(self):
        csv_datas = self.upload_file
        fileobj = TemporaryFile('wb+')
        csv_datas = base64.decodebytes(csv_datas)
        fileobj.write(csv_datas)
        fileobj.seek(0)
        str_csv_data = fileobj.read().decode('utf-8')
        lis = csv.reader(io.StringIO(str_csv_data), delimiter=',')
        row_num = 0
        DATE_FORMAT = '%m/%d/%Y'
        not_process_plan = []
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
                    process_plan_ob_id = value[1].strip() or False
                    # dt_cr = False
                    # dt_wr = False
                    # if creation_date:
                    #     dt_cr = datetime.datetime.strptime(creation_date.split('.')[0], '%Y-%m-%d %H:%M:%S').strftime(
                    #         '%Y-%m-%d %H:%M:%S')
                    #     print("date>>>>>", name, dt_cr)
                    # if update_date:
                    #     dt_wr = datetime.datetime.strptime(update_date.split('.')[0], '%Y-%m-%d %H:%M:%S').strftime(
                    #         '%Y-%m-%d %H:%M:%S')
                    #     print("date>>>>>", name, dt_wr)
                    # org_id = []
                    # c_id = []
                    # w_id = []
                    activity_id = []
                    route_id = []
                    # if ad_org_id:
                    #     org_id = self.env['esmech.organization'].search(
                    #         [('ob_id', '=', ad_org_id)])
                    # if created_by:
                    #     c_id = self.env['res.users'].search(
                    #         [('user_ob_id', '=', created_by)])
                    # if write_by:
                    #     w_id = self.env['res.users'].search(
                    #         [('user_ob_id', '=', write_by)])
                    if process_plan_ob_id:
                        route_id = self.env['mrp.routing'].search(
                            [('process_plan_ob_id', '=', process_plan_ob_id)])
                        if not route_id:
                            not_process_plan.append(process_plan_ob_id)
                    print("process_plan", not_process_plan)
            except Exception as e:
                _logger.error('------------Error Exception---------- %s', e, value[18])
                error_list.append(value)
        return error_list
