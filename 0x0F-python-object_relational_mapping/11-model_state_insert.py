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

    session.add(State(name="Louisiana"))
    session.commit()
    state_new = session.query(State).order_by(State.id.desc()).first()

    print(state_new.id)
    session.close()