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

from odoo import models, fields, api


class OpAttendanceRegister(models.Model):
    _name = 'op.attendance.register'
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    name = fields.Char(
        'Name', size=16, required=True, track_visibility='onchange')
    code = fields.Char(
        'Code', size=8, required=True, track_visibility='onchange')
    course_id = fields.Many2one(
        'op.course', 'Course', required=True, track_visibility='onchange')
    batch_id = fields.Many2one(
        'op.batch', 'Batch', required=True, track_visibility='onchange')
    subject_id = fields.Many2one(
        'op.subject', 'Subject', track_visibility='onchange')

    @api.onchange('course_id')
    def onchange_course(self):
        self.batch_id = False
