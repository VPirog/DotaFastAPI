from sqlalchemy import Column, Integer, Float, CHAR
from sqlalchemy.orm import relationship

from database import Base


class Item(Base):
    __tablename__ = 'item'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(CHAR(50))
    price = Column(Integer)
    strenght = Column(Integer)
    agility = Column(Integer)
    intelligence = Column(Integer)
    health = Column(Integer)
    mana = Column(CHAR(10))
    hp_regen = Column(Float)
    mana_regen = Column(Float)
    armor = Column(Integer)
    evasion = Column(Integer)
    magic_resistance = Column(Integer)
    spell_amp = Column(Integer)
    damage = Column(CHAR(20))
    attack_speed = Column(Integer)
    movement_speed = Column(CHAR(10))
    item_type = Column(CHAR(16))
    img = Column(CHAR(99))

    items = relationship("ItemGuide", back_populates="item")

    def __str__(self):
        return f"Айтем {self.id}: {self.name}"
