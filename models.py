# Having these separate Python files is good because you can use the same model to query or load data outside of an app.

from sqlalchemy import Column, Integer, Float, String
# from sqlalchemy.types import Date
from database import Base


class Measurement(Base):
    __tablename__ = "measurement"
    id = Column(Integer, primary_key=True)
    station = Column(String)
    date = Column(String)
    prcp = Column(Float)
    tobs = Column(Float)


class Station(Base):
    __tablename__ = "station"
    id = Column(Integer, primary_key=True)
    station = Column(String)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)
