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

import random

from .accept import AcceptHeaderProvider


class HeaderProvider(AcceptHeaderProvider):
    """ HeaderProvider class"""

    def __init__(self, config, agent_list=()):
        """
        Init interface. Accept external params
        :param src.lib.browser.config.Config config: browser configurations
        :param dict agent_list: user agent list
        """

        self.__headers = {}
        self.__cfg = config
        self.__agent_list = agent_list

        AcceptHeaderProvider.__init__(self)

        # custom header
        self.init_headers()

    @property
    def __user_agent(self):
        """
        Get user agent
        :return: str
        """

        if True is self.__cfg.is_random_user_agent:
            index = random.randrange(0, len(self.__agent_list))
            user_agent = self.__agent_list[index].strip()
        else:
            user_agent = self.__cfg.user_agent
        return user_agent

    def init_headers(self):
        # --cookie "a=1&b=2"  ->  cookie: a=1; b=2;
        if self.__cfg.cookie != '':
            self.add_header('Cookie', self.__cfg.cookie.replace('&', '; ')+ ';')

        # --header "X-Forwarded-For: 127.0.0.1" --header "Content-Type: image/jpeg"
        for _h in self.__cfg.header:
            if ':' not in _h: # sanity check
                continue
            key, value = _h.split(':', 1)
            self.add_header(key.strip(), value.strip())

    def add_header(self, key, value):
        """
        Add custom header

        :param str key: header name
        :param str value: header value
        :return: HeaderProvider
        """

        self.__headers[key] = value

        return self

    def add_header_default(self, key, value):
        if key not in self.__headers:
            self.add_header(key, value)

    @property
    def _headers(self):
        """
        Get Headers
        :return: dict headers
        """

        self.add_header_default('Accept', self._accept)
        self.add_header_default('Accept-Encoding', self._accept_encoding)
        self.add_header_default('Accept-Language', self._accept_language)
        self.add_header_default('Referer', ''.join([self.__cfg.scheme, self.__cfg.host]))
        self.add_header_default('User-Agent', self.__user_agent)
        self.add_header_default('Cache-Conrol', 'no-cache')
        self.add_header_default('Connection', 'close')
        self.add_header_default('Pragma', 'no-cache')
        if 'Cookie' in self.__headers:
            __cookie = self.__headers.pop('Cookie')
            self.add_header('Cookie', __cookie)

        return self.__headers
