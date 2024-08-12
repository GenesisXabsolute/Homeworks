from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import Annotated, List

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
async def read_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int):
    try:
        current_index = users[-1].id + 1
        user = User(id=current_index, username=username, age=age)
        users.append(user)
    except IndexError:
        user = User(id=1, username=username, age=age)
        users.append(user)
    return user


@app.put('/user/{user_id}/{username}/age')
async def update_user(user_id: int, username: str, age: int):
    for i in users:
        if i.id == user_id:
            i.username = username
            i.age = age
            return i
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    for i in users:
        if i.id == user_id:
            c = users.index(i)
            a = users.pop(c)
            return a
    raise HTTPException(status_code=404, detail="User was not found")
