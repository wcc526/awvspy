# -*- coding: utf-8 -*-
"""
awvspy.awvsresult
~~~~~~~~~~~~~~~~~~

This module contains the awvs scan result.
"""

import sys
import logging
import hashlib
import datetime
from sqlalchemy.dialects import registry
from sqlalchemy import create_engine
from awvspy.awvsmodels import AWVSScans,AWVSAlerts,AWVSAlerts2refXREF,AWVSSiteFiles
import json
from awvspy.dbapi import make_session_scope,get_session,AlchemyEncoder

registry.register("access", "sqlalchemy_access.pyodbc", "AccessDialect_pyodbc")
registry.register("access.pyodbc", "sqlalchemy_access.pyodbc", "AccessDialect_pyodbc")


if sys.platform == 'win32':
    import pyodbc

class AWVSResult(object):

    def __init__(self):
        pass

engine = create_engine("access+pyodbc://vulnscanresults")
session = get_session(engine=engine)
with make_session_scope(session) as session:
    wvs_scans = session.query(AWVSSiteFiles).all()
    for wvs_scan in wvs_scans:
        print json.dumps(wvs_scan,cls=AlchemyEncoder)
