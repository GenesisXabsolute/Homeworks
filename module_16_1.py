from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def read_users_admin() -> str:
    return "Вы зашли как администратор"


@app.get("/user/{user_id}")
async def read_users(user_id: int) -> str:
    return f"Вы зашли как пользователь № {user_id}"


@app.get("/user")
async def read_users_id(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
