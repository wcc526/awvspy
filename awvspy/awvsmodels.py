# -*- coding: utf-8 -*-
"""
awvspy.awvsmodels
~~~~~~~~~~~~~~~~~~

This module contains the awvs scan models.
"""

import logging
LOG = logging.getLogger(__name__)
from sqlalchemy.dialects import registry
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from awvspy.packages.sqlalchemy_access.sqlalchemy_access.base import AcInteger,AcString,AcDateTime,AcBoolean

registry.register("access", "sqlalchemy_access.pyodbc", "AccessDialect_pyodbc")
registry.register("access.pyodbc", "sqlalchemy_access.pyodbc", "AccessDialect_pyodbc")

BASE = declarative_base()

class WVSScans(BASE):

    __tablename__ = 'WVS_scans'

    scid = Column(AcInteger,primary_key=True)
    grid = Column(AcInteger)
    starturl = Column(AcDateTime)
    starttime = Column(AcDateTime)
    finishtime = Column(AcDateTime)
    aborted = Column(AcBoolean)
    responsive = Column(AcBoolean)
    serverid = Column(AcInteger)

    def __repr__(self):
        return "%s|%s|%s|%s|%s|%s|%s|%s" % (self.scid,self.grid,self.starturl,self.starttime,self.finishtime,self.aborted,self.responsive,self.serverid)
