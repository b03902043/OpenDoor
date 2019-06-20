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

import re
from .provider import ResponsePluginProvider


class Real200ResponsePlugin(ResponsePluginProvider):
    """ Real200ResponsePlugin class"""

    DESCRIPTION = 'Custom 404 (detect custom 404 pages)'
    RESPONSE_INDEX = 'real200'
    DEFAULT_STATUSES = [200, 201, 202, 203, 204, 205, 206, 207, 208]

    def __init__(self):
        """
        ResponsePluginProvider constructor
        """

        ResponsePluginProvider.__init__(self)

    def process(self, response):
        """
        Process data
        :return: str
        """

        if response.status in self.DEFAULT_STATUSES:
            super().process(response)

            # vars:   _body
            if 0 < len(self._body) and self._status in self.DEFAULT_STATUSES:
                if not 'Not Found' in self._body:   return self.RESPONSE_INDEX
        return "404" # None == pass to another sniffer. see src/core/http/providers/response.py for detailed 
