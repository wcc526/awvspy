# -*- coding: utf-8 -*-

"""
AWVS Python library
~~~~~~~~~~~~~~~~~~~~~

"""

__title__ = 'awvs python library'
__version__ = '0.0.1'
__build__ = 0x000001
__author__ = 'wcc526'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2015 wcc526'

from . import utils
from .models import *
from .api import *
from .status_codes import *
from .exceptions import *

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
