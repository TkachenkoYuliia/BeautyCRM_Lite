from sqlalchemy import Column, Integer, Boolean, DateTime, Float, String, ForeignKey
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
    __tablename__ = 'services'
    brows = "brows"
    hair = "hair"
    nails = "nails"

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True, index=True)
    client = Column(String, ForeignKey('clients.name'))
    master = Column(String, ForeignKey('users.username'))
    service = Column(String, ForeignKey('services.name'))
    price = Column(Float, index=True)
    is_paid = Column(Boolean, index=True)
    status = Column(String, index=True)
    created_at = Column(DateTime, index=True)