from sqlalchemy import Column, Integer, String, ForeignKey
from orm.db_connection import Base, create_tables


class Temp(Base):
    __tablename__ = 'temp'

    id = Column(Integer, primary_key=True)
    id_terra = Column(String(16))
    temp = Column(String(16))