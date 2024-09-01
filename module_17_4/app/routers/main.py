from fastapi import FastAPI
from app.models import task, user

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router2)
app.include_router(task.router)
