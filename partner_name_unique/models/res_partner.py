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
            results = self.env['res.partner'].search_count([
                ('name', 'ilike', partner.name.strip())
            ])
            if results > 1:
                raise ValidationError(
                    _("The name must be unique per partner!"))
