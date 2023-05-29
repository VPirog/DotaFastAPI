from sqlalchemy import Column, Integer, CHAR, SmallInteger, Float

from database import Base


class Hero(Base):
    __tablename__ = 'hero'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(CHAR(30), nullable=False)
    base_strength = Column(SmallInteger, nullable=False)
    base_agility = Column(SmallInteger, nullable=False)
    base_intelligence = Column(SmallInteger, nullable=False)
    str_gain = Column(Float, nullable=False)
    agi_gain = Column(Float, nullable=False)
    int_gain = Column(Float, nullable=False)
    base_armor = Column(Float, nullable=False)
    base_magic_res = Column(Float, nullable=False)
    base_move_speed = Column(SmallInteger, nullable=False)
    attack_type = Column(CHAR(6))
    img = Column(CHAR(99))



    def __str__(self):
        return f"{self.name}"
