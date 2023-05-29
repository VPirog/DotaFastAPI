from sqlalchemy import Column, Integer, Float, CHAR, ForeignKey
from database import Base


class Admin(Base):
    __tablename__ = 'admin'
    __table_args__ = {'extend_existing': True}


    id = Column(ForeignKey('user.id'), primary_key=True)
    nickname = Column(CHAR(99), nullable=False)
    password = Column(CHAR(20), nullable=False)
    email = Column(CHAR(30), nullable=False)