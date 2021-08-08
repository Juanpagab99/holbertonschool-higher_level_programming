#!/usr/bin/python3
"""delete states"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

from sqlalchemy.orm.session import Session
from sqlalchemy.sql import base
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                    argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).\
            filter(State.name.like('%a%')):
        session.delete(state)
    session.commit()
    session.close()
