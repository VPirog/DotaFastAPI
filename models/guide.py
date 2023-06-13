from typing import List
from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from database import Guide

GuideOut = sqlalchemy_to_pydantic(Guide)


class GuideIn(sqlalchemy_to_pydantic(Guide)):
    class Config:
        orm_mode = True


GuideIn.__fields__.pop('id')
print(GuideIn.__fields__)


class GuidesOut(BaseModel):
    students: List[GuideOut]
