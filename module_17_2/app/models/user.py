from fastapi import APIRouter
from app.backend.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from app.models import *

router2 = APIRouter(prefix='/user', tags=['user'])


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship("Task", back_populates="user")


@router2.get('/')
async def all_users():
    pass


@router2.get('/user_id')
async def user_by_id():
    pass


@router2.post('/create')
async def create_user():
    pass


@router2.put('/update')
async def update_user():
    pass


@router2.delete('/delete')
async def delete_user():
    pass


from sqlalchemy.schema import CreateTable

print(CreateTable(User.__table__))
