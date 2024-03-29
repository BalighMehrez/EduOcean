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
    'name': 'EduOcean Parent',
    'version': '10.0.3.0.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Parent',
    'complexity': "easy",
    'author': 'Tech Receptives',
    'website': 'http://www.dataocean.com',
    'depends': ['eduocean_core'],
    'data': [
        'security/op_parent_security.xml',
        'data/parent_user_data.xml',
        'views/parent_view.xml',
        'parent_menu.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [
        'demo/res_partner_demo.xml',
        'demo/res_users_demo.xml',
        'demo/parent_demo.xml',
    ],
    'images': [
        'static/description/eduocean_parent_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
