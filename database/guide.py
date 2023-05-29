from sqlalchemy import Column, Integer, Float, CHAR, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Guide(Base):
    __tablename__ = 'guide'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(CHAR(99))
    rating = Column(Float(53))
    description = Column(CHAR(399))
    main_text = Column(CHAR(9999))
    owner_user_id = Column(ForeignKey('user.id'))
    hero_id = Column(ForeignKey('hero.id'))
    main_text = Column(CHAR(9999))

    hero = relationship('Hero')
    owner_user = relationship('User')

    guides = relationship("ItemGuide", back_populates="guide")
    guideS_rating = relationship("UserRating", back_populates="guide_rating")
    guide_comments = relationship("GuideCommentary", back_populates="guide_comment")

    def __str__(self):
        return f"gaid {self.id}: {self.name} {self.description}"

    def __lt__(self, other):
        return self.id < other.id
