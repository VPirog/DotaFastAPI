from sqlalchemy import Column, Integer, Float, CHAR
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(CHAR(99), nullable=False)
    password = Column(CHAR(20), nullable=False)
    country = Column(CHAR(20), nullable=False)

    userS_rating = relationship("UserRating", back_populates="user_rating")
    user_comments = relationship("GuideCommentary", back_populates="user_comment")

    def __str__(self):
        return f"юзер {self.id}: {self.username} {self.password}"
