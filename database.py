from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# PostgreSQL database URL
DATABASE_URL = "postgresql://raviyadav:newpassword@localhost/customer_success"

# Create database engine
engine = create_engine(DATABASE_URL)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Database Model
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    available = Column(Boolean, default=True)


# Prevent DB creation during tests
if os.getenv("TESTING") != "true":
    Base.metadata.create_all(bind=engine)


# Create tables
# Base.metadata.create_all(bind=engine)
