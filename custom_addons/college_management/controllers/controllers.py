# -*- coding: utf-8 -*-
# from odoo import http


# class CollegeManagement(http.Controller):
#     @http.route('/college_management/college_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/college_management/college_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('college_management.listing', {
#             'root': '/college_management/college_management',
#             'objects': http.request.env['college_management.college_management'].search([]),
#         })

#     @http.route('/college_management/college_management/objects/<model("college_management.college_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('college_management.object', {
#             'object': obj
#         })
