from pydantic import BaseModel
from datetime import datetime

# class User(BaseModel):
#     username: str
#     email: str
#     password: str

class User(BaseModel):
    id: int
    username: str
    service: str

    class Config:
        from_attributes = True

class Services(BaseModel):
    service: str

class Client(BaseModel):
    id: int
    name: str
    phone: str

    class Config:
        from_attributes = True

class Appointment(BaseModel):
    client: Client
    master: User
    service: str
    price: float
    is_paid: bool
    status: str
    created_at: datetime.datetime

    class Config:
        from_attributes = True