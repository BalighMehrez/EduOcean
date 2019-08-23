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

from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SessionReport(models.TransientModel):
    _name = 'time.table.report'
    _description = 'Generate Time Table Report'

    state = fields.Selection(
        [('teacher', 'Teacher'), ('student', 'Student')],
        string='Select', required=True, default='teacher')
    course_id = fields.Many2one('op.course', 'Course')
    batch_id = fields.Many2one('op.batch', 'Batch')
    teacher_id = fields.Many2one('op.teacher', 'Teacher')
    start_date = fields.Date(
        'Start Date', required=True,
        default=(datetime.today() - relativedelta(
            days=datetime.date(
                datetime.today()).weekday())).strftime('%Y-%m-%d'))
    end_date = fields.Date(
        'End Date', required=True,
        default=(datetime.today() + relativedelta(days=6 - datetime.date(
            datetime.today()).weekday())).strftime('%Y-%m-%d'))

    @api.multi
    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for session in self:
            start_date = fields.Date.from_string(session.start_date)
            end_date = fields.Date.from_string(session.end_date)
            if end_date < start_date:
                raise ValidationError(_('End Date cannot be set before \
                Start Date.'))
            elif end_date > (start_date + timedelta(days=6)):
                raise ValidationError(_("Select date range for a week!"))

    @api.onchange('course_id')
    def onchange_course(self):
        if self.batch_id and self.course_id:
            if self.batch_id.course_id != self.course_id:
                self.batch_id = False

    @api.multi
    def gen_time_table_report(self):
        data = self.read(
            ['start_date', 'end_date', 'course_id', 'batch_id', 'state',
             'teacher_id'])[0]
        if data['state'] == 'student':
            time_table_ids = self.env['op.session'].search(
                [('course_id', '=', data['course_id'][0]),
                 ('batch_id', '=', data['batch_id'][0]),
                 ('start_datetime', '>', data['start_date'] + '%H:%M:%S'),
                 ('end_datetime', '<', data['end_date'] + '%H:%M:%S')],
                order='start_datetime asc')

            data.update({'time_table_ids': time_table_ids.ids})
            return self.env['report'].get_action(
                self, 'eduocean_timetable.report_timetable_student_generate',
                data=data)
        else:
            teacher_time_table_ids = self.env['op.session'].search(
                [('start_datetime', '>', data['start_date'] + '%H:%M:%S'),
                 ('end_datetime', '<', data['end_date'] + '%H:%M:%S'),
                 ('teacher_id', '=', data['teacher_id'][0])],
                order='start_datetime asc')

            data.update({'teacher_time_table_ids': teacher_time_table_ids.ids})
            return self.env['report'].get_action(
                self, 'eduocean_timetable.report_timetable_teacher_generate',
                data=data)