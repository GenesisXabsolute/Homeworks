from pydantic import BaseModel
from typing import Annotated, List
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, HTTPException, Path, Request

app = FastAPI()
templates = Jinja2Templates(directory='templates')

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/')
async def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/users/{user_id}')
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id]})


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


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: int = Path(ge=1, le=100),
                username: str = Path(min_length=5, max_length=20, description='Enter username'),
                age: int = Path(ge=18, le=120, description='Enter age')) -> str:
    User.username = username
    User.age = age
    User.user_id = user_id - 1
    return f'User <{user_id}> has been updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(ge=1, le=100)):
    try:
        users.pop(user_id - 1)
        return f'The user <{user_id}> has been deleted.'
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")