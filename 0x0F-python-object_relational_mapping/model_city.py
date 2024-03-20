#!/usr/bin/python3
"""Python file that contains the class definition of a city
and an instance Base = declarative_base()"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import sys
from model_state import Base

Base = declarative_base()


class State(Base):
    """
    Class that represents a state in the database.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
