# -*- coding: utf-8 -*-
###############################################################################
#
#    DataOcean Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY DataOcean(<http://www.dataocean.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import models, fields, api


class WizardOpTeacher(models.TransientModel):
    _name = 'wizard.op.teacher'
    _description = "Create User for selected Teacher(s)"

    def _get_teachers(self):
        if self.env.context and self.env.context.get('active_ids'):
            return self.env.context.get('active_ids')
        return []

    teacher_ids = fields.Many2many(
        'op.teacher', default=_get_teachers, string='Teachers')

    @api.multi
    def create_teacher_user(self):
        user_group = self.env.ref('eduocean_core.group_op_teacher')
        active_ids = self.env.context.get('active_ids', []) or []
        records = self.env['op.teacher'].browse(active_ids)
        self.env['res.users'].create_user(records, user_group)
