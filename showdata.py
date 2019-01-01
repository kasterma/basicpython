"""Create updating plot over time of data generated"""

from time import sleep

from bokeh.models import ColumnDataSource
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

from bokeh.layouts import column
from bokeh.plotting import figure, curdoc

engine = create_engine("sqlite:///test.sqlite")
Session = sessionmaker(engine)
session = Session()

Base = declarative_base()


class DataPt(Base):
    __tablename__ = "testdata"

    idx = Column(Integer, primary_key=True)
    val = Column(Float)


plot = figure()
source = ColumnDataSource(data={'x': [0,1,2],'y': [0,2,2]})  # dummy data to start with
plot.line(x='x', y='y', source=source)


def update_data():
    dat = pd.read_sql(session.query(DataPt).order_by(DataPt.idx).statement, session.bind)
    source.data = dict(x=dat.idx, y=dat.val)
    print("hello")
    sleep(1)


def main():
    update_data()
    curdoc().add_root(column(plot))
    curdoc().add_periodic_callback(update_data, 100)

main()