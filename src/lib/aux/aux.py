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

import itertools

class Aux(object):
    """ User defined functions """

    @staticmethod
    def generate(*wordlist_args, **kwargs):
        # ex. generate(wordlist1, wordlist2)
        fn = kwargs.get('handle') or Aux.identity
        fn_args = kwargs.get('handle_params')
        for _ in itertools.product(*wordlist_args):
            url = fn(None, fn_args) # src/lib/reader/reader.py _directories__line
            for _url in Aux.decorate(url, *_):
                yield _url
    
    @staticmethod
    def decorate(url, *args):
        # ex. decorate(word1, word2)
        transform = Aux.identity
        args = list(map(Aux._trim, args))
        turl = url.replace('FUZZ', transform(args[0], 0))
        for i, arg in enumerate(args[1:]):
            turl = turl.replace('FUZ%dZ'%(i+2), transform(arg, i))
        yield turl

    @staticmethod
    def _trim(w):
        w = ''.join(map(chr, w))
        w = w.rstrip('\n').rstrip('\r')
        return w

    @staticmethod
    def identity(x, *args, **kwargs):
        return x

