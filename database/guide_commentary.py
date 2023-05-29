from sqlalchemy import Column, Text, Integer, ForeignKey, CHAR
from sqlalchemy.orm import relationship

from .base_meta import Base


class GuideCommentary(Base):
    __tablename__ = 'guide_commentary'
    __table_args__ = {'extend_existing': True}

    guide_id = Column(ForeignKey('guide.id'), primary_key=True, nullable=False)
    user_id = Column(ForeignKey('user.id'), primary_key=True, nullable=False)
    commentary = Column(CHAR(199))

    guide_comment = relationship("Guide", back_populates="guide_comments")
    user_comment = relationship("User", back_populates="user_comments")
