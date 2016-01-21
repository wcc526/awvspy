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
from awvspy.packages.sqlalchemy_access.sqlalchemy_access.base import AcInteger

registry.register("access", "sqlalchemy_access.pyodbc", "AccessDialect_pyodbc")
registry.register("access.pyodbc", "sqlalchemy_access.pyodbc", "AccessDialect_pyodbc")

BASE = declarative_base()

class WVSScans(BASE):

    __tablename__ = 'WVS_scans'

    scid = Column(AcInteger,primary_key=True)

    def __repr__(self):
        return "%s" % (self.scid)
