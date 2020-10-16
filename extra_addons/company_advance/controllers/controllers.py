# -*- coding: utf-8 -*-
# from odoo import http


# class CompanyAdvance(http.Controller):
#     @http.route('/company_advance/company_advance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/company_advance/company_advance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('company_advance.listing', {
#             'root': '/company_advance/company_advance',
#             'objects': http.request.env['company_advance.company_advance'].search([]),
#         })

#     @http.route('/company_advance/company_advance/objects/<model("company_advance.company_advance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('company_advance.object', {
#             'object': obj
#         })
