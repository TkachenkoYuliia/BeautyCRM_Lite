from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    service: str

    class Config:
        orm_mode = True

class Client(BaseModel):
    id: int
    name: str
    phone: str

    class Config:
        orm_mode = True

class Appointment(BaseModel):
    client: Client
    master: User
    service: str
    price: float
    is_paid: bool
    status: str
    #created_at: datetime


    class Config:
        orm_mode = True