# -*- coding: utf-8 -*-
# from odoo import http


# class DrTraining(http.Controller):
#     @http.route('/dr_training/dr_training', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dr_training/dr_training/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dr_training.listing', {
#             'root': '/dr_training/dr_training',
#             'objects': http.request.env['dr_training.dr_training'].search([]),
#         })

#     @http.route('/dr_training/dr_training/objects/<model("dr_training.dr_training"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dr_training.object', {
#             'object': obj
#         })
