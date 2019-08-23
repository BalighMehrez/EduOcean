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


class WizardOpTeacherEmployee(models.TransientModel):
    _name = 'wizard.op.teacher.employee'
    _description = "Create Employee and User of Teacher"

    user_boolean = fields.Boolean("Want to create user too ?", default=True)

    @api.multi
    def create_employee(self):
        for record in self:
            active_id = self.env.context.get('active_ids', []) or []
            teacher = self.env['op.teacher'].browse(active_id)
            teacher.create_employee()
            if record.user_boolean and not teacher.user_id:
                user_group = self.env.ref('eduocean_core.group_op_teacher')
                self.env['res.users'].create_user(teacher, user_group)
