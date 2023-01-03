from .database import Base
from sqlalchemy import Column, String, Integer


class Cars_DB(Base):
    __tablename__ = "Cars"
    id = Column(Integer, primary_key=True, index=True)
    car_number = Column(String)


