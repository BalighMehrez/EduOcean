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
from odoo.exceptions import ValidationError, Warning


class OpAssignmentSubLine(models.Model):
    _name = 'op.assignment.sub.line'
    _inherit = 'mail.thread'
    _rec_name = 'assignment_id'
    _description = 'Assignment Submission'

    assignment_id = fields.Many2one(
        'op.assignment', 'Assignment', required=True)
    student_id = fields.Many2one(
        'op.student', 'Student',
        default=lambda self: self.env['op.student'].search(
            [('user_id', '=', self.env.uid)]), required=True)
    description = fields.Text('Description', track_visibility='onchange')
    state = fields.Selection(
        [('draft', 'Draft'), ('submit', 'Submitted'), ('reject', 'Rejected'),
         ('change', 'Change Req.'), ('accept', 'Accepted')], 'State',
        default='draft', track_visibility='onchange')
    submission_date = fields.Datetime(
        'Submission Date', readonly=True,
        default=lambda self: fields.Datetime.now(), required=True)
    note = fields.Text('Note')
    user_id = fields.Many2one(
        'res.users', related='student_id.user_id', string='User')
    teacher_user_id = fields.Many2one(
        'res.users', related='assignment_id.teacher_id.user_id',
        string='Teacher User')

    @api.multi
    def act_draft(self):
        result = self.state = 'draft'
        return result and result or False

    @api.multi
    def act_submit(self):
        result = self.state = 'submit'
        return result and result or False

    @api.multi
    def act_accept(self):
        result = self.state = 'accept'
        return result and result or False

    @api.multi
    def act_change_req(self):
        result = self.state = 'change'
        return result and result or False

    @api.multi
    def act_reject(self):
        result = self.state = 'reject'
        return result and result or False

    @api.multi
    def unlink(self):
        for record in self:
            if not record.state == 'draft' and not self.env.user.has_group(
                    'eduocean_core.group_op_teacher'):
                raise ValidationError(
                    _("You can't delete none draft submissions!"))
        res = super(OpAssignmentSubLine, self).unlink()
        return res

    @api.model
    def create(self, vals):
        if self.env.user.child_ids:
            raise Warning(_('Invalid Action!\n Parent can not \
            create Assignment Submissions!'))
        return super(OpAssignmentSubLine, self).create(vals)

    @api.multi
    def write(self, vals):
        if self.env.user.child_ids:
            raise Warning(_('Invalid Action!\n Parent can not edit \
            Assignment Submissions!'))
        return super(OpAssignmentSubLine, self).write(vals)
