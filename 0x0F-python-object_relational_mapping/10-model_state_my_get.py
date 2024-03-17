#!/usr/bin/python3
"""  script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa via sqlalchemy"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    name = argv[4]

    results = session.query(State).filter(State.name.like(name))

    if results is None:
        print("Not found")
    else:
        print(results[0].id)
