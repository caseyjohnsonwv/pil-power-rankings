from typing import Generator
import uuid
from contextlib import contextmanager
from sqlalchemy import Column, DateTime, Float, Integer, String, ForeignKeyConstraint
from sqlalchemy.engine import create_engine, Engine
from sqlalchemy.orm import DeclarativeBase, Session


def get_engine(echo:bool=True) -> Engine:
    return create_engine('sqlite:///pil.db', echo=echo)

@contextmanager
def get_session():
    try:
        engine = get_engine(echo=False)
        session = Session(bind=engine)
        yield session
    finally:
        session.close()
        engine.dispose()


def generate_uuid_pk():
    return str(uuid.uuid4())


class Base(DeclarativeBase):
    pass

class Team(Base):
    __tablename__ = 'teams'
    id = Column('id', String, primary_key=True, default=generate_uuid_pk)
    name = Column('name', String, unique=True)

class Player(Base):
    __tablename__ = 'players'
    account_id = Column('account_id', String, primary_key=True)
    username = Column('username', String)
    team_id = Column('team_id', String, nullable=True)
    __table_args__ = (
        ForeignKeyConstraint(['team_id'], ['teams.id'], onupdate='CASCADE', ondelete='CASCADE'),
    )

class Map(Base):
    __tablename__ = 'maps'
    uid = Column('uid', String, primary_key=True)
    name = Column('name', String)
    totd_date = Column('totd_date', DateTime, nullable=True)

class Record(Base):
    __tablename__ = 'records'
    id = Column('id', String, primary_key=True, default=generate_uuid_pk)
    account_id = Column('account_id', String)
    map_uid = Column('map_uid', String)
    time = Column('time', Float)
    position = Column('position', Integer)
    __table_args__ = (
        ForeignKeyConstraint(['map_uid'], ['maps.uid'], onupdate='CASCADE', ondelete='CASCADE'),
    )
