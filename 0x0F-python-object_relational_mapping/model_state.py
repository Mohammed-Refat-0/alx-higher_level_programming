#!/usr/bin/python3
"""python file that contains the class definition of a State
and an instance Base = declarative_base()"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


engine = create_engine(
    'mysql+pymysql://username:password@localhost:3306/database_name')

Base.metadata.create_all(engine)
