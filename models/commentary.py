from typing import List
from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from database import GuideCommentary

CommentOut = sqlalchemy_to_pydantic(GuideCommentary)


class CommentIn(sqlalchemy_to_pydantic(GuideCommentary)):
    class Config:
        orm_mode = True




class CommentsOut(BaseModel):
    comments: List[CommentOut]
