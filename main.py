from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    account: str
    last_name: str
    first_name: str
    email: str
    age: Union[int, None] = None


app = FastAPI()


@app.post("/users/")
async def create_user(user: User):
    return user
