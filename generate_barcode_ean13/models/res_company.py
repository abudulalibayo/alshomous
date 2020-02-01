# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields, models, _


class ResCompany(models.Model):
    _inherit = "res.company"

    code_entreprise = fields.Char("Code entreprise",size=3)