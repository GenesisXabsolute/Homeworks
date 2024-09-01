from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db import Base
from app.backend.db_depends import get_db
from typing import Annotated
from app.routers.schemas import CreateUser, UpdateUser, CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from app.models import *


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True, index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship('User', back_populates='task')


router = APIRouter(prefix='/tasks', tags=['tasks'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    temp = db.scalars(select(Task).where(Task.completed is Task.completed)).all()
    return temp


@router.get('/task_id')
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.scalars(select(Task).where(Task.id == task_id)).first()
    if result is not None:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')


@router.post('/create')
async def create_task(current_task: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)]):
    try:
        task = db.execute(insert(Task).values(title=current_task.title,
                                              content=current_task.content,
                                              priority=current_task.priority,
                                              user_id=user_id,
                                              slug=slugify(current_task.title)))
        db.commit()
        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
    except Exception as e:
        raise HTTPException(status_code=404, detail='User was not found')


@router.put('/update')
async def update_task(task_id: int, current_task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    result = db.scalars(select(Task).where(Task.id == task_id)).first()
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')
    db.execute(update(Task).where(Task.id == task_id).values(title=current_task.title,
                                                             content=current_task.content,
                                                             priority=current_task.priority))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.delete('/delete')
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.scalars(select(Task).where(Task.id == task_id)).first()
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task delete is successful!'}
