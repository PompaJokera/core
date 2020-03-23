from sqlalchemy import Column, Integer, String, ForeignKey
from orm.db_connection import Base, create_tables


class User(Base):
    __tablename__ = 'terrariums'

    id = Column(Integer, primary_key=True)
    id_terra = Column(String(16))
    temp = Column(String(16))
    name = Column(String(16))