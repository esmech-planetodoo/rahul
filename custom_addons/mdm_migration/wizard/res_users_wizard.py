
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


class ResUsers(models.TransientModel):
    _name = 'import.res.users'

    upload_file = fields.Binary(string='File URL')

    def import_apartments(self):

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
                    _logger.info('-----row number %s', key)
                    ad_user_id = value[0] or False
                    ad_client_id = value[1] or False
                    ad_org_id = value[2] or False
                    isactive = value[3] or False
                    created = value[4] or False
                    createdby = value[5] or False
                    updated = value[6] or False
                    updatedby = value[7] or False
                    name = value[8].strip() or False
                    description = value[9].strip() or False
                    password = value[10].strip() or False
                    email = value[11].strip() or False
                    supervisor_id = value[12] or False
                    c_bpartner_id = value[13] or False
                    processing = value[14].strip() or False
                    emailuser = value[15].strip() or False
                    emailuserpw = value[16].strip() or False
                    c_bpartner_location_id = value[17] or False
                    c_greeting_id = value[18] or False
                    title = value[19].strip() or False
                    comments = value[20].strip() or False
                    phone = value[21] or False
                    phone2 = value[22] or False
                    fax = value[23] or False
                    lastcontact = value[24] or False
                    lastresult = value[25] or False
                    birthday = value[26] or False
                    ad_orgtrx_id = value[27] or False
                    firstname = value[28].strip() or False
                    lastname = value[29].strip() or False
                    username = value[30].strip() or False
                    default_ad_client_id = value[31] or False
                    default_ad_language = value[32] or False
                    default_ad_org_id = value[33] or False
                    default_ad_role_id = value[34] or False
                    default_m_warehouse_id = value[35] or False
                    islocked = value[36] or False
                    ad_image_id = value[37].strip() or False
                    grant_portal_access = value[38] or False
                    em_esmpur_department = value[39] or False
                    em_extl_tallyusername = value[40].strip() or False
                    dt_birth = False
                    dt_last = False
                    if lastcontact:
                        dt_last = datetime.datetime.strptime(lastcontact, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
                        print("date>>>>>",name,dt_last)
                    if birthday:
                        dt_birth = datetime.datetime.strptime(birthday, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
                        print("date>>>>>",name,dt_birth)
                    org_id = []
                    dept_id = []
                    wh_id = []
                    org_id_self = []
                    if em_esmpur_department:
                        dept_id = self.env['extc.department'].search([('department_ob_id', '=', em_esmpur_department)])
                    if default_ad_org_id:
                        org_id = self.env['esmech.organization'].search(
                            [('ob_id', '=', default_ad_org_id)])
                    if ad_org_id:
                        org_id_self = self.env['esmech.organization'].search(
                            [('ob_id', '=', ad_org_id)])
                    if default_m_warehouse_id:
                        wh_id = self.env['stock.warehouse'].search(
                            [('ob_id', '=', default_m_warehouse_id)])
                    user_vals = {
                        'user_ob_id': ad_user_id,
                        'ad_client_id': ad_client_id,
                        'ad_org': org_id_self.id if org_id_self else False,
                        'name': name,
                        # 'password': password,
                        'firstname': firstname,
                        'lastname': lastname,
                        'username': username,
                        'login': username,
                        'tally_username': em_extl_tallyusername,
                        'description': description,
                        'active': isactive,
                        'ob_department_id': dept_id.id if dept_id else False,
                        # 'business_partner': C_BPartner_ID.id,
                        'is_locked': islocked,
                        'birthday': dt_birth if dt_birth else False,
                        'phone': phone,
                        'mobile': phone2,
                        'fax': fax,
                        'email': email,
                        'email_server_username': emailuser,
                        # 'supervisor': supervisor_id.id,
                        # 'default_role': default_ad_role_id,
                        'comment':comments,
                        'greeting_id':c_greeting_id,
                        'grant_portal_access':grant_portal_access,
                        'processing':processing,
                        'lastcontact':dt_last if dt_last else False,
                        'lastresult':lastresult,
                        'organization_ids': [(0,0,{
                            'res_users_id': org_id.id,
                            'name': org_id.name,
                            'search_key':org_id.search_key,
                            'description':org_id.description,
                            'is_active':org_id.is_active,
                            'summary_level':org_id.summary_level,
                            'legal_name':org_id.legal_name,
                            'gstin_no':org_id.gstin_no,
                            'exporter_reference_no':org_id.exporter_reference_no,

                        })] if org_id else False,
                        'default_warehouse_id': wh_id.id if wh_id else  False,

                    }
                    print("name>>>>>", )
                    # lines = [(5,0,0)]
                    if user_vals:
                        supplier_id = self.env['res.users'].create(user_vals)

            except Exception as e:
                _logger.error('------------Error Exception---------- %s', e, value[0])
                error_list.append(value)


