# -*- coding: utf-8 -*-
# Copyright 2018 Tecnativa - David Vidal
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class PosSaleReport(models.Model):
    _inherit = "report.pos.order"

    product_brand_id = fields.Many2one('product.brand',string='Brand')

    def _select(self):
        select_str = super(PosSaleReport, self)._select()
        select_str += """
            , pt.product_brand_id
            """
        return select_str

    def _group_by(self):
        group_by_str = super(PosSaleReport, self)._group_by()
        group_by_str += ", pt.product_brand_id"
        return group_by_str
