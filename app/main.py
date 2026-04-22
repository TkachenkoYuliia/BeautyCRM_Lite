from fastapi import FastAPI, HTTPException, Path, Query, Body, Depends
from typing import Optional, List, Dict, Annotated

from schemas import User, Client, Appointment
from models import User as User_model, Client, Service
import datetime

app = FastAPI()


@app.post("/users/")
async def create_user(user: User):
    return {"Master is ": user.username}

@app.get("/services/")
async def get_service(services: Service):
    if services is Service.brows:
        return {"The service: ": services, "do": "Marina"}

    if services.value == "hair":
        return {"Your hair": services, "makes": "brilliants"}

    return {"Nails": services, "message": "Have some painting nails"}


@app.get("/users/{user_id}")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
