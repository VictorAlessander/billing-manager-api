from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import configure

configs = configure()
engine = create_engine(
    configs["conn"]["database_uri"], connect_args={"check_same_thread": False}
)
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
