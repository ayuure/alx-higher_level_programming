#!/usr/bin/python3
"""Create states table in hbtn_0e_0_usa with some data"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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

    for instance in session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id
    ):
        print(instance[0] + ": (" + str(instance[1]) + ") " + instance[2])
    session.close()
