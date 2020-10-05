from sqlalchemy import Column, Integer, DateTime, ForeignKey
from ..base.base import Base
from datetime import datetime
from ..devices import Devices
from ..sensor import Sensor


class Relay(Base):
    __tablename__ = 'relay'
    id = Column(Integer, primary_key=True)
    dev_id = Column(Integer, ForeignKey(Devices.id), nullable=False, index=True)
    sensor_id = Column(Integer, ForeignKey(Sensor.id), nullable=False, index=True)
    slot = Column(Integer)
    value = Column(Integer)
    time = Column(DateTime(), default=datetime.now())
