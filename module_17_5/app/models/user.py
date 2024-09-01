from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db import Base
from app.backend.db_depends import get_db
from typing import Annotated
from app.routers.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from app.models.task import Task

router2 = APIRouter(prefix='/user', tags=['user'])


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    task = relationship('Task', back_populates='user')


@router2.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User).where(User.id == User.id)).all()
    return users


@router2.get('/user_id')
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.scalars(select(User).where(User.id == user_id)).first()
    if result is not None:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')


@router2.get('/user_id/tasks')
async def user_by_id_tasks(user_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    if result is not None:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')


@router2.post('/create')
async def create_user(current_user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(User).where(current_user.username == User.username)).first()
    if result is None:
        db.execute(insert(User).values(username=current_user.username,
                                       firstname=current_user.firstname,
                                       lastname=current_user.lastname,
                                       age=current_user.age,
                                       slug=slugify(current_user.username)))

        db.commit()
        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
    db.commit()


@router2.put('/update')
async def update_user(user_id: int, db: Annotated[Session, Depends(get_db)], current_user: UpdateUser):
    result = db.scalars(select(User).where(User.id == user_id))
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    db.execute(update(User).where(User.id == user_id).values(firstname=current_user.firstname,
                                                             lastname=current_user.lastname,
                                                             age=current_user.age,
                                                             slug=slugify(current_user.firstname)))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router2.delete('/delete')
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.scalars(select(User).where(User.id == user_id)).first()
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    db.execute(delete(Task).where(Task.user_id == user_id))
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User delete is successful!'}
