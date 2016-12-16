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

import common


RBD = None
WBD = None
IBD = None


# Specific "mod_import" function for python 2.6 support as importlib is new in python 2.7
# Support for python2.6 is being dropped and backend management have to be refactored.
def mod_import(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


if common.config.get('read_backend', 'type'):
    try:
        RBD = mod_import(common.config.get('read_backend', 'type'))
        RBD.configure(dict(common.config.items('read_backend')))
    except Exception as err:
        raise RuntimeError(err)

if common.config.get('write_backend', 'type'):
    try:
        WBD = mod_import(common.config.get('write_backend', 'type'))
        WBD.configure(dict(common.config.items('write_backend')))
    except Exception as err:
        raise RuntimeError(err)

if common.config.get('info_backend', 'type'):
    try:
        IBD = mod_import(common.config.get('info_backend', 'type'))
        IBD.configure(dict(common.config.items('info_backend')))
    except Exception as err:
        raise RuntimeError(err)
