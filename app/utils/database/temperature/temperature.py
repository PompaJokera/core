from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from ..base.base import Base
from datetime import datetime
from ..devices import Devices
from ..sensor import Sensor


class Temperature(Base):
    __tablename__ = 'temperature'
    id = Column(Integer, primary_key=True)
    dev_id = Column(Integer, ForeignKey(Devices.id), nullable=False, index=True)
    sensor_id = Column(Integer, ForeignKey(Sensor.id), nullable=False, index=True)
    value = Column(Float)
    time = Column(DateTime(), default=datetime.now())
