# -*- coding: utf-8 -*-

from odoo import models, fields, api

class telenoc_city(models.Model):
    _inherit = 'res.partner'

    city = fields.Char(default="Riyadh")
    country_id = fields.Many2one(default=192)
