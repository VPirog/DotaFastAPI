from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from models import UserIn, UserOut, UsersOut
from database import get_session, User

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: int,
                   session: Session = Depends(get_session)):
    user: User = session.query(User).get(user_id)
    if user:
        user_dto = UserOut(**user.__dict__)
        return user_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"User with id {user_id} not found!")


# @router.get("/get_all", response_model=UserOut)
# async def get_all(session: Session = Depends(get_session)):
#     session = get_session()
#     users: User = session.query(User).all()
#     user_dto = list(map(lambda user: UserOut(**user.__dict__), users))
#     return UsersOut(users=user_dto)


@router.post("/", response_model=UserOut)
async def create_user(user: UserIn):
    session = get_session()
    orm_user = User(**user.dict())
    session.add(orm_user)
    session.commit()
    user_dto = UserOut(**orm_user.__dict__)
    return user_dto


@router.delete("/delete/{user_id}")
async def delete_user(user_id: int,
                      session: Session = Depends(get_session)):
    user: User = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
        raise HTTPException(status_code=200,
                            detail=f"User with id {user_id} deleted!")

    else:
        raise HTTPException(status_code=404,
                            detail=f"User with id {user_id} not found!")


@router.put("/update/{user_id}")
async def update_user(user: UserIn,
                      user_id: int,
                      session: Session = Depends(get_session)):
    server_user: User = session.query(User).get(user_id)
    if user:
        server_user.username = user.username
        server_user.password = user.password
        server_user.country = user.country
        session.commit()
        return UserOut(**server_user.__dict__)
    else:
        raise HTTPException(status_code=404,
                            detail=f"User with id {user_id} not found!")
