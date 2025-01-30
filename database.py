from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

# Check if we are running tests by checking the TESTING environment variable
if os.getenv("TESTING") == "true":
    print("Running tests")
    DATABASE_URL = "sqlite:///./test.db"  # Set the test database URL
else:
    print("Running app")
    load_dotenv()  # Load environment variables from .env file for production or dev
    DATABASE_URL = os.getenv("DATABASE_URL")  # Get DATABASE_URL from .env

# Print to verify which DB URL is being loaded
print(DATABASE_URL)

# Create database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})

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
