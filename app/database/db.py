from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session
from sqlalchemy.orm.session import sessionmaker

from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

Base = declarative_base()


def create_session():
    session = scoped_session(sessionmaker(bind=engine))
    return session


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)
