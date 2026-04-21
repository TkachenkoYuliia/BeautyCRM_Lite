from fastapi import FastAPI
from schemas import User, Client, Appointment
from models import User, Client
import datetime

app = FastAPI()


@app.post("/users/"):
async def create_user(user: User):
    return {"message": "Hello World"}

@app.get("/users/{user_id}")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
