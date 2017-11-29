# -*- coding: utf-8 -*-
# Copyright 2017 Grant Thornton Spain - Ismael Calvo <ismael.calvo@es.gt.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import SavepointCase
from odoo.exceptions import ValidationError


class TestNameUnique(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestNameUnique, cls).setUpClass()
        cls.partner = cls.env['res.partner'].create({
            'name': ' Partner Name ',
        })

    def test_duplicated_name_creation(self):
        with self.assertRaises(ValidationError):
            self.env['res.partner'].create({
                'name': 'partner name ',
            })
