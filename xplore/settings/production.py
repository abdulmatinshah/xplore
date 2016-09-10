from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

try:
    from .dev import *
except ImportError:
    pass
