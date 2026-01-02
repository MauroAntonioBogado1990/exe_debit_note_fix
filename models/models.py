# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class exe_debit_note_fix(models.Model):
#     _name = 'exe_debit_note_fix.exe_debit_note_fix'
#     _description = 'exe_debit_note_fix.exe_debit_note_fix'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
