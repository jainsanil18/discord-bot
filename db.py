from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import Config
#connect the sqlalchemy framework to the db
engine = create_engine(Config.POSTGRES_URL, echo = True)
Base = declarative_base()
#define configuration of a db session
Session = sessionmaker(bind = engine)