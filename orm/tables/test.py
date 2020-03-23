from sqlalchemy import Column, Integer, String, ForeignKey
from orm.db_connection import Base, db_session_add, create_tables


class Temp(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    id_test = Column(Integer)
    temp = Column(String(16))


def add_temp(temperature):
    temp = Temp()
    temp.id_test = 1
    temp.temp = f"{temperature}"
    db_session_add(temp)


create_tables()
