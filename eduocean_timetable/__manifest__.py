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
    'name': 'EduOcean Timetable',
    'version': '10.0.3.0.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage TimeTables',
    'complexity': "easy",
    'author': 'Tech Receptives',
    'website': 'http://www.dataocean.com',
    'depends': ['eduocean_classroom'],
    'data': [
        'views/timetable_view.xml',
        'views/timing_view.xml',
        'views/teacher_view.xml',
        'report/report_timetable_student_generate.xml',
        'report/report_timetable_teacher_generate.xml',
        'report/report_menu.xml',
        'wizard/generate_timetable_view.xml',
        'wizard/time_table_report.xml',
        'dashboard/timetable_student_dashboard.xml',
        'dashboard/timetable_teacher_dashboard.xml',
        'security/ir.model.access.csv',
        'security/op_timetable_security.xml',
        'timetable_menu.xml',
        'wizard/session_confirmation.xml',
        'views/timetable_templates.xml',
    ],
    'demo': [
        'demo/timing_demo.xml',
        'demo/op_timetable_demo.xml'
    ],
    'test': [
        'test/timetable_sub_value.yml',
        'test/generate_timetable.yml'
    ],
    'images': [
        'static/description/eduocean_timetable_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
