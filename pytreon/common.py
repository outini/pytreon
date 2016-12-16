#
#    Monitoring control python module (pytreon)
#
#    Copyright (C) 2014 Denis Pompilio (jawa) <denis.pompilio@gmail.com>
#
#    This file is part of pytreon
#
#    This program is free software; you can redistribute it and/or
#    modify it under the terms of the GNU General Public License
#    as published by the Free Software Foundation; either version 2
#    of the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, see <http://www.gnu.org/licenses/>.

"""
Common tools for Pytreon
"""

try:
    # import python2.7 module
    from ConfigParser import SafeConfigParser
except ImportError:
    from configparser import SafeConfigParser


_config_file = "etc/pytreon.cfg"


try:
    config = SafeConfigParser()
    config.read(_config_file)
except IOError as err:
    print(err)


class GenericEntity(object):
    """Generic entity class to store monitoring related entities
    """
    def __init__(self):
        self.name = None

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if self.name is None:
            return NotImplemented
        if hasattr(other, "name"):
            return other.name == self.name
        return NotImplemented

    def __ne__(self, other):
        eq = self.__eq__(other)
        if eq is NotImplemented:
            return NotImplemented
        return not eq


def indent(text, lvl=1):
    """Indent a block of text
    """
    space = "{0}".format(lvl * 4 * " ")
    separator = "\n{0}".format(space)
    return "{0}{1}\n".format(space, separator.join(text.rstrip().split('\n')))
