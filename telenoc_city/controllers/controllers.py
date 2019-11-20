# -*- coding: utf-8 -*-
from odoo import http

# class TelenocCity(http.Controller):
#     @http.route('/telenoc_city/telenoc_city/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/telenoc_city/telenoc_city/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('telenoc_city.listing', {
#             'root': '/telenoc_city/telenoc_city',
#             'objects': http.request.env['telenoc_city.telenoc_city'].search([]),
#         })

#     @http.route('/telenoc_city/telenoc_city/objects/<model("telenoc_city.telenoc_city"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('telenoc_city.object', {
#             'object': obj
#         })