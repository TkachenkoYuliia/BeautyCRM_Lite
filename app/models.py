from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from enum import Enum

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    service = Column(String, unique=True, index=True)


class Client(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    author = relationship(User)

class Service(str, Enum):
        brows = "brows"
        hair = "hair"
        nails = "nails"

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True, index=True)