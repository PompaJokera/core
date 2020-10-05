from sqlalchemy import Column, Integer, DateTime, ForeignKey
from ..base.base import Base
from datetime import datetime
from ..devices import Devices
from ..sensor import Sensor


class Door(Base):
    __tablename__ = 'door'
    id = Column(Integer, primary_key=True)
    dev_id = Column(Integer, ForeignKey(Devices.id), nullable=False, index=True)
    sensor_id = Column(Integer, ForeignKey(Sensor.id), nullable=False, index=True)
    value = Column(Integer)
    time = Column(DateTime(), default=datetime.now())
