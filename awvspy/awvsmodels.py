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
from awvspy.packages.sqlalchemy_access.sqlalchemy_access.base import AcInteger,AcString,AcDateTime,AcBoolean,AcTinyInteger,AcText,AcUnicode,AcChar

registry.register("access", "sqlalchemy_access.pyodbc", "AccessDialect_pyodbc")
registry.register("access.pyodbc", "sqlalchemy_access.pyodbc", "AccessDialect_pyodbc")

BASE = declarative_base()

class AWVSScans(BASE):
    """Contains the mapping of awvs scan task info"""

    __tablename__ = 'WVS_scans'

    # scan id
    scid = Column(AcInteger,primary_key=True)
    #
    grid = Column(AcInteger,nullable=False)
    # which url you start scan
    starturl = Column(AcText,nullable=True)
    starttime = Column(AcDateTime,nullable=True)
    finishtime = Column(AcDateTime,nullable=True)
    # if the scan is aborted
    aborted = Column(AcBoolean,nullable=True)
    # if the target server has responsive
    responsive = Column(AcBoolean,nullable=True)
    # the target server id
    serverid = Column(AcInteger,nullable=True)

class AWVSAlerts(BASE):
    """Contains the mapping of awvs scan results"""

    __tablename__ = 'WVS_alerts'

    # scan id
    scid = Column(AcInteger,primary_key=True)
    # alert id
    alid = Column(AcInteger,primary_key=True)
    # which module found  vulnerability
    modulename = Column(AcText)
    # vulnerability group
    algroup = Column(AcText)
    # affects which file
    affects = Column(AcText)
    affects_det = Column(AcText)
    # the page parameter
    parameter = Column(AcText)
    # the serverity level
    severity = Column(AcInteger)
    # the vulnerability class
    classname = Column('class',AcString)
    # the detail vulnerability
    details = Column(AcText)
    impact_id = Column(AcInteger)
    desc_id = Column(AcInteger)
    recm_id = Column(AcInteger)
    detdesc_id = Column(AcInteger)
    # the xml path
    alertpath = Column(AcText)
    alerttags = Column(AcText)
    compinfo = Column(AcText)
    # the http request
    request = Column(AcText)
    # the http response
    response = Column(AcText)

class AWVSAlerts2refXREF(BASE):

    __tablename__ = 'WVS_alerts2refs_XREF'

    # scan id
    scid = Column(AcInteger,primary_key=True)
    # alert id
    alid = Column(AcInteger,primary_key=True)
    # which module found  vulnerability
    refid = Column(AcInteger,primary_key=True)

class AWVSSiteFiles(BASE):

    __tablename__ = 'WVS_site_files'

    # scan id
    scid = Column(AcInteger,primary_key=True)
    # alert id
    sfid = Column(AcInteger,primary_key=True)
    # url
    url = Column(AcText,primary_key=True)
    wasscanned = Column(AcBoolean)
    vulnerable = Column(AcBoolean)
