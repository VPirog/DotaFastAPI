from typing import List
from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from database import User

UserOut = sqlalchemy_to_pydantic(User)


class UserIn(sqlalchemy_to_pydantic(User)):
    class Config:
        orm_mode = True


UserIn.__fields__.pop('id')
print(UserIn.__fields__)


class UsersOut(BaseModel):
    students: List[UserOut]
