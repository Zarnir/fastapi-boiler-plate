from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = Base

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(100), nullable=False)
    created_at: datetime = Column(DateTime, server_default="now()")
    updated_at: datetime = Column(DateTime, server_default="now()")
