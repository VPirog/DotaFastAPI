from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class ItemGuide(Base):
    __tablename__ = 'item_guide'
    __table_args__ = {'extend_existing': True}

    guide_id = Column(ForeignKey('guide.id'), primary_key=True, nullable=False)
    item_id = Column(ForeignKey('item.id'), primary_key=True, nullable=False)

    guide = relationship("Guide", back_populates="guides")
    item = relationship("Item", back_populates="items")
