from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Annotated, List

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def read_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return 'User {username} registered.'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: int) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return 'User {username} registered.'


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    users.pop(str(user_id))
