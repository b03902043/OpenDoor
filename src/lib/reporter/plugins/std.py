# -*- coding: utf-8 -*-

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Development Team: Stanislav WEB
"""

from .provider import PluginProvider

class StdReportPlugin(PluginProvider):
    """ StdReportPlugin class"""

    def __int__(self):
        """
        Init provider
        :return: None
        """
        PluginProvider.__init__(self)
        self.data = {}

    def set_report_data(self, data):
        self.data = data

    def get_report_data(self):
        return self.data

