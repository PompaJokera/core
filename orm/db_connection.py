from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:terrarium@db/terra', echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()


def create_tables():
    Base.metadata.create_all(engine)


def db_session_add(obj):
    session = Session()
    session.add(obj)
    session.commit()
    session.close()
