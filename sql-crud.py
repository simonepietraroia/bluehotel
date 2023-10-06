from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///hmzmzlan")
base = declarative_base()

class Guest(base):
    __tablename_ = "Guest-Booking"
    id = Column(Interger, primary_key=True)
    x = Column(String)
    x = Column(String)
    x = Column(String)
    x = Column(String)


Session = sessionmaker(db)

session = Session()

base.metadata.create_all(db)
