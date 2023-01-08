from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class players(Base):
    __tablename__ = "players"

    playerId = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    height = Column(Float, default=True)
    date_of_birth = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String, index=True)



class country(Base):
    __tablename__ = "country"

    countryId = Column(Integer, primary_key=True, index=True)
    country_name = Column(String, index=True)
    continent = Column(String)



class club(Base):
    __tablename__ = "club"

    clubId = Column(Integer, primary_key=True, index=True)
    club_name = Column(String, index=True)
    club_value = Column(String)




