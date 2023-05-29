from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class UserRating(Base):
    __tablename__ = 'user_rating'
    __table_args__ = {'extend_existing': True}

    user_id = Column(ForeignKey('user.id'), primary_key=True, nullable=False)
    guide_id = Column(ForeignKey('guide.id'), primary_key=True, nullable=False)
    rating = Column(Integer)

    user_rating = relationship("User", back_populates="userS_rating")
    guide_rating = relationship("Guide", back_populates="guideS_rating")
