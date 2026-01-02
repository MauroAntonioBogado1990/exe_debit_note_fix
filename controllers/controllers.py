# -*- coding: utf-8 -*-
# from odoo import http


# class ExeDebitNoteFix(http.Controller):
#     @http.route('/exe_debit_note_fix/exe_debit_note_fix/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/exe_debit_note_fix/exe_debit_note_fix/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('exe_debit_note_fix.listing', {
#             'root': '/exe_debit_note_fix/exe_debit_note_fix',
#             'objects': http.request.env['exe_debit_note_fix.exe_debit_note_fix'].search([]),
#         })

#     @http.route('/exe_debit_note_fix/exe_debit_note_fix/objects/<model("exe_debit_note_fix.exe_debit_note_fix"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('exe_debit_note_fix.object', {
#             'object': obj
#         })
