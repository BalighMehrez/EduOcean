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

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class OpExamSession(models.Model):
    _name = 'op.exam.session'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _description = 'Exam Session'

    name = fields.Char(
        'Exam Session', size=256, required=True, track_visibility='onchange')
    course_id = fields.Many2one(
        'op.course', 'Course', required=True, track_visibility='onchange')
    batch_id = fields.Many2one(
        'op.batch', 'Batch', required=True, track_visibility='onchange')
    exam_code = fields.Char(
        'Exam Session Code', size=8,
        required=True, track_visibility='onchange')
    start_date = fields.Date(
        'Start Date', required=True, track_visibility='onchange')
    end_date = fields.Date(
        'End Date', required=True, track_visibility='onchange')
    exam_ids = fields.One2many(
        'op.exam', 'session_id', 'Exam(s)')
    exam_type = fields.Many2one(
        'op.exam.type', 'Exam Type',
        required=True, track_visibility='onchange')
    evaluation_type = fields.Selection(
        [('normal', 'Normal'), ('grade', 'Grade')],
        'Evolution type', default="normal",
        required=True, track_visibility='onchange')
    venue = fields.Many2one(
        'res.partner', 'Venue', track_visibility='onchange')

    @api.constrains('start_date', 'end_date')
    def _check_date_time(self):
        if self.start_date > self.end_date:
            raise ValidationError(_(
                'End Date cannot be set before Start Date.'))

    @api.onchange('course_id')
    def onchange_course(self):
        self.batch_id = False
