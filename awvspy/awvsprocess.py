# -*- coding: utf-8 -*-
"""
awvspy.awvsprocess
~~~~~~~~~~~~~~~~~~

This module contains the awvs process console command.
"""

import os
import logging
import sys
import re

LOG = logging.getLogger(__name__)

if sys.platform == 'win32':
    import _winreg

class AWVSProcess(object):
    """The :class:`AWVS Process` object,which contains awvs console command
    """

    def __init__(self):
        self.awvspath = self._get_awvs_console_path()

    def _get_awvs_console_path(self):
        """Return

        """
        try:
            conn = _winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE)
            wvs_path = _winreg.QueryValue(conn, 'SOFTWARE\Classes\Acunetix_WVS_Scan\Shell\Open\Command')
            _winreg.CloseKey(conn)
            wvs_path = re.search('"([^"]*)"', wvs_path).group(1)
            wvs_dir = os.path.dirname(wvs_path)
            return os.path.join(wvs_dir, 'wvs_console.exe')
        except Exception, e:
            LOG.error(e, exc_info=True)
