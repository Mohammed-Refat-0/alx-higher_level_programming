#!/usr/bin/python3
"""Python file that contains the class definition of a State
and an instance Base = declarative_base()"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://root:root@localhost/hbtn_0e_6_usa',
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
