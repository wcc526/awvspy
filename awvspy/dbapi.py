# -*- coding: utf-8 -*-
from contextlib import contextmanager
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
import json

@contextmanager
def make_session_scope(Session):
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def get_session(engine):
    session = scoped_session(sessionmaker(bind=engine))
    return session

class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        # an SQLAlchemy class
        fields = {}
        for field in [x for x in obj.__dict__ if not x.startswith('_') and x != 'metadata']:
            data = obj.__getattribute__(field)
            try:
                json.dumps(data)  # this will fail on non-encodable values, like other classes
                fields[field] = data
            except TypeError:
                fields[field] = None
        return fields
