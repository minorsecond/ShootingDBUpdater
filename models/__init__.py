from datetime import datetime

from geoalchemy2 import *
from sqlalchemy import Column, BigInteger, String, DateTime, \
    Integer, Boolean, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

from common import get_conf

conf = get_conf()

con_string = f"postgresql://{conf['pg_user']}:{conf['pg_pw']}@" \
                 f"{conf['pg_host']}/{conf['pg_db']}"

engine = create_engine(con_string)
Base = declarative_base(metadata=MetaData(schema='police_shootings'))

__all__ = ["engine", 'Shooting']


class Shooting(Base):
    """
    A shooting event
    """

    __tablename__ = "shooting"
    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=True)
    date = Column(DateTime, nullable=True)
    manner_of_death = Column(String, nullable=True)
    armed = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    gender = Column(String, nullable=True)
    race = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    signs_of_mental_illness = Column(Boolean, nullable=True)
    threat_level = Column(String, nullable=True)
    flee = Column(String, nullable=True)
    body_camera = Column(Boolean, nullable=True)
    is_geocoding_exact = Column(Boolean, nullable=True)
    geom = Column(Geometry(geometry_type='POINT', srid=4326), nullable=True)
    date_added = Column(DateTime, default=datetime.utcnow())


Shooting.__table__.create(engine, checkfirst=True)
