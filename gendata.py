"""Generate some data and put in it a database.

This is to have a data source from which to then run a bokeh visualization.
"""
from time import sleep

from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import numpy as np

engine = create_engine("sqlite:///test.sqlite")
Session = sessionmaker(engine)
session = Session()

Base = declarative_base()


class DataPt(Base):
    __tablename__ = "testdata"

    idx = Column(Integer, primary_key=True)
    val = Column(Float)


Base.metadata.create_all(engine)


def main():
    index = 0
    value = 0.0
    while True:
        index += 1
        value += np.random.uniform(0, 1)
        dat = DataPt(idx=index, val=value)
        session.add(dat)
        session.commit()
        sleep(1)


if __name__ == "__main__":
    main()
