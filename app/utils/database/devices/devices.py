from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from ..base.base import Base
from datetime import datetime


class Devices(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True)
    friendly_name = Column(String(15), nullable=False, index=True)
    ip = Column(String(15))
    last_update = Column(DateTime(), default=datetime.now())
