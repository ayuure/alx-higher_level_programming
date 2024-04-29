#!/usr/bin/python3
"""Create states table in hbtn_0e_0_usa with some data"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_a = session.query(State).filter(State.name.like("%a")).all()

    for state in state_a:
        print(state.id, state.name, sep=": ")

    session.close()