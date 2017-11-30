# -*- coding: utf-8 -*-
# Copyright 2017 Grant Thornton Spain - Ismael Calvo <ismael.calvo@es.gt.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('vat')
    def _check_vat_unique(self):
        results = self.env['res.partner'].read_group([
            ('parent_id', '=', False),
            ('vat', 'in', map(lambda p: p.vat, filter(lambda p: p.vat, self)))
        ], ['vat'], ['vat'])
        for result in results:
            if result.get('vat_count') > 1:
                raise ValidationError(
                    _("The VAT must be unique per partner!"))
