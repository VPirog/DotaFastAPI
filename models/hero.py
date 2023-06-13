from typing import List
from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from database import Hero

HeroOut = sqlalchemy_to_pydantic(Hero)


class HeroIn(sqlalchemy_to_pydantic(Hero)):
    class Config:
        orm_mode = True


HeroIn.__fields__.pop('id')
print(HeroIn.__fields__)


class HeroesOut(BaseModel):
    students: List[HeroOut]
