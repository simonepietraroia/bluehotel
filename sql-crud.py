from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///hmzmzlan")
base = declarative_base()

class 


Session = sessionmaker(db)

session = Session()

base.metadata.create_all(db)
