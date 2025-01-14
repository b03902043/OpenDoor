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

import codecs
import collections
import json
import re
import webbrowser
from urllib.parse import urlparse, quote
from distutils.version import LooseVersion


class Helper(object):

    """Helper class"""

    @staticmethod
    def counter():
        """
        Provide counter collection
        :return: collections.Counter
        """

        return collections.Counter()

    @staticmethod
    def list():
        """
        Provide dictionary collection
        :return: dict
        """

        container = collections.defaultdict(list)
        return container

    @staticmethod
    def parse_url(url):
        """
        Parse url

        :param str url: input url
        :return: dict
        """

        # for ascii >= 128
        #url = ''.join(map(lambda x: '%{:02x}'.format(ord(x)) if ord(x) >= 128 else x, url))
        pobj = urlparse(url)
        pobj = pobj._replace(path=quote(pobj.path+pobj.fragment))

        return pobj

    @staticmethod
    def to_json(data, sort=True, indents=4):
        """
        Json pretty print
        :param dict data: mixed data params
        :param bool sort: use sort
        :param int indents: space indents
        :return: str
        """

        json_data = json.dumps(data, sort_keys=sort, indent=indents)
        return json_data

    @staticmethod
    def openbrowser(target):
        """
        Open target path in local browser
        :param string target: url or local path
        :return: bool
        """

        return webbrowser.open(target)

    @staticmethod
    def percent(counter=0, total=1):
        """
        Return percentage
        :param int counter: current value
        :param int total: total value
        :return: str
        """

        return "{percent}%".format(percent=round(100.0 * counter / float(total), 1))

    @staticmethod
    def is_less(arg1, arg2):
        """
        Compare two numbers (< less)
        :param int arg1: right version
        :param int arg2: left version
        :return: bool
        """

        return LooseVersion(arg1) < LooseVersion(arg2)

    @staticmethod
    def is_more(arg1, arg2):
        """
        Compare two numbers (great >)
        :param int arg1: right version
        :param int arg2: left version
        :return: bool
        """

        return LooseVersion(arg1) > LooseVersion(arg2)

    @staticmethod
    def is_callable(func):
        """
        Check if function is callable

        :param callable func:
        :return: bool
        """

        return isinstance(func, collections.Callable)

    @staticmethod
    def decode_hostname(hostname):
        """
        Decode non-latin hostname

        param str hostname: input string
        :return: str
        """

        domain = hostname.strip().encode().decode('utf8')
        return str(domain.encode("idna").decode("utf-8"))

    @staticmethod
    def decode(s, errors='strict'):
        """
        Decode strings

        :param str s: input string
        :param str errors:error level
        :return: s
        """

        output = ''
        try:
            if len(s) < 3:
                if codecs.BOM_UTF8.startswith(s):
                    # not enough data to decide if this is a BOM
                    # => try again on the next call
                    output = ""

            elif s[:3] == codecs.BOM_UTF8:
                (output, sizes) = codecs.utf_8_decode(s[3:], errors)
            elif s[:3] == codecs.BOM_UTF16:
                output = s[3:].decode('utf16')
            else:
                # (else) no BOM present
                (output, sizes) = codecs.utf_8_decode(s, errors)
            return s(output)
        except (UnicodeDecodeError, Exception):
            # seems, its getting not a content (images, file, etc)
            try:
                return s.decode('cp1251')
            except (UnicodeDecodeError, Exception):
                return ""

    @staticmethod
    def filter_directory_string(s):
        """
        Filter directory string

        :param str s: input string
        :return: str
        """

        s = s.strip("\n")
        s = s.lstrip("/")

        return s.strip()

    @staticmethod
    def filter_domain_string(s):
        """
        Filter domain/subdomain string

        :param str s: input string
        :return: str
        """

        s = s.strip('\n')
        s = re.sub(r'[^\w\d_-]', '', s).lower()
        if not s:
            s = '_'
        return s.lower()
