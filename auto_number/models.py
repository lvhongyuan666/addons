# -*- coding: utf-8 -*-
import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)


class TestAuto(models.Model):
    _name = 'auto_number.test'
    _description = '测试自动创建流程编号'

    name = fields.Char(string='编号', required=True, default=lambda self: '新建')
    reason = fields.Char(string='原由')

    @api.model
    def create(self, vals):
        if vals.get('name', '新建') == '新建':
            vals['name'] = self.env['ir.sequence'].next_by_code('auto_number.test')

        return super(TestAuto, self).create(vals)


