# -*- coding: utf-8 -*-
# Copyright 2017 Grant Thornton Spain - Ismael Calvo <ismael.calvo@es.gt.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        name = vals.get('name', False)
        if name:
            vals['name'] = name.strip()
        return super(ResPartner, self).create(vals)

    @api.multi
    def write(self, vals):
        name = vals.get('name', False)
        if name:
            vals['name'] = name.strip()
        return super(ResPartner, self).write(vals)

    @api.constrains('name')
    def _check_name_unique(self):
        for partner in self:
            self._cr.execute(u"""
                SELECT id
                FROM res_partner
                WHERE name ilike '{}'
            """.format(partner.name))
            if (len(self._cr.dictfetchall()) > 1):
                raise ValidationError(
                    _("The name must be unique per partner!"))
