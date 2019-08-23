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

{
    'name': 'EduOcean Assignment',
    'version': '10.0.3.0.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Assgiments',
    'complexity': "easy",
    'author': 'Tech Receptives',
    'website': 'http://www.dataocean.com',
    'depends': ['eduocean_core', 'base_action_rule'],
    'data': [
        'security/ir.model.access.csv',
        'security/op_assignment_security.xml',
        'views/assignment_view.xml',
        'views/assignment_type_view.xml',
        'views/assignment_sub_line_view.xml',
        'views/student_view.xml',
        'dashboard/assignment_student_dashboard.xml',
        'dashboard/assignment_teacher_dashboard.xml',
        'assignment_menu.xml',
        'data/action_rule_data.xml',
    ],
    'demo': [
        'demo/assignment_type_demo.xml',
        'demo/assignment_demo.xml',
        'demo/assignment_sub_line_demo.xml'
    ],
    'test': [
        'test/res_users_test.yml',
        'test/assignment_sub_values.yml',
        'test/assignment_creation_submission.yml'
    ],
    'images': [
        'static/description/eduocean_assignment_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
