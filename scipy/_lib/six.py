"""Utilities for writing code that runs on Python 2 and 3"""

# Copyright (c) 2010-2012 Benjamin Peterson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import operator
import sys

__author__ = "Benjamin Peterson <benjamin@python.org>"
__version__ = "1.2.0"


string_types = str,
integer_types = int,
class_types = type,
text_type = str
binary_type = bytes

MAXSIZE = sys.maxsize


def _add_doc(func, doc):
    """Add documentation to a function."""
    func.__doc__ = doc


def _import_module(name):
    """Import module, returning the module after the last dot."""
    __import__(name)
    return sys.modules[name]


# Replacement for lazy loading stuff in upstream six.  See gh-2764
import builtins
import functools
reduce = functools.reduce
zip = builtins.zip
xrange = builtins.range


_meth_func = "__func__"
_meth_self = "__self__"

_func_code = "__code__"
_func_defaults = "__defaults__"

_iterkeys = "keys"
_itervalues = "values"
_iteritems = "items"

try:
    advance_iterator = next
except NameError:
    def advance_iterator(it):
        return it.next()
next = advance_iterator


def get_unbound_function(unbound):
    return unbound


Iterator = object

def callable(obj):
    return any("__call__" in klass.__dict__ for klass in type(obj).__mro__)


_add_doc(get_unbound_function,
         """Get the function out of a possibly unbound function""")


get_method_function = operator.attrgetter(_meth_func)
get_method_self = operator.attrgetter(_meth_self)
get_function_code = operator.attrgetter(_func_code)
get_function_defaults = operator.attrgetter(_func_defaults)


def iterkeys(d):
    """Return an iterator over the keys of a dictionary."""
    return iter(getattr(d, _iterkeys)())


def itervalues(d):
    """Return an iterator over the values of a dictionary."""
    return iter(getattr(d, _itervalues)())


def iteritems(d):
    """Return an iterator over the (key, value) pairs of a dictionary."""
    return iter(getattr(d, _iteritems)())


def b(s):
    return s.encode("latin-1")

def u(s):
    return s


if sys.version_info[1] <= 1:
    def int2byte(i):
        return bytes((i,))
else:
    # This is about 2x faster than the implementation above on 3.2+
    int2byte = operator.methodcaller("to_bytes", 1, "big")
import io
StringIO = io.StringIO
BytesIO = io.BytesIO

_add_doc(b, """Byte literal""")
_add_doc(u, """Text literal""")


import builtins
exec_ = getattr(builtins, "exec")

def reraise(tp, value, tb=None):
    if value.__traceback__ is not tb:
        raise value.with_traceback(tb)
    raise value


print_ = getattr(builtins, "print")
del builtins

_add_doc(reraise, """Reraise an exception.""")


def with_metaclass(meta, base=object):
    """Create a base class with a metaclass."""
    return meta("NewBase", (base,), {})
