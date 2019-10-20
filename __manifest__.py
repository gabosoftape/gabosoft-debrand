# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2019-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Tintuk Tomin(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': "Odoo Debranding",
    'version': "13.0.1.0.0",
    'summary': """Debrand Odoo""",
    'description': """Debrand Odoo,Debranding""",
    'author': "Cybrosys Techno Solutions",
    'company': "Cybrosys Techno Solutions",
    'maintainer': "Cybrosys Techno Solutions",
    'website': "https://cybrosys.com/",
    'category': 'Tools',
    'depends': ['base', 'im_livechat', 'website'],
    'data': [
        'views/views.xml'
    ],
    'qweb': ["static/src/xml/base.xml"],
    'images': ['static/description/banner.png'],
    'license': "AGPL-3",
    'installable': True,
    'application': False
}
