# -*- coding: utf-8 -*-
from contextlib import contextmanager
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

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
