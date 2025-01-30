import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from main import app
from dotenv import load_dotenv
import os

# SQLite in-memory database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

print("DATABASE_URL for tests SQLALCHEMY_DATABASE_URL:", SQLALCHEMY_DATABASE_URL) 

# Create a new engine and sessionmaker for testing
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables in the test database
Base.metadata.create_all(bind=engine)

# Override the get_db dependency for testing
@pytest.fixture(scope="function")
def db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a TestClient instance
client = TestClient(app)

# Test case for GET /items/
def test_create_item(db):
    item_data = {"name": "Test Item", "description": "Test description", "price": 20.0, "available": True}
    
    # Create the item
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    created_item = response.json()
    
    # Verify item was created correctly
    assert created_item["name"] == item_data["name"]
    assert created_item["price"] == item_data["price"]
    
    # Retrieve the created item
    item_id = created_item["id"]
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    retrieved_item = response.json()
    
    # Verify the retrieved item matches the created item
    assert retrieved_item["id"] == item_id
    assert retrieved_item["name"] == item_data["name"]
    assert retrieved_item["price"] == item_data["price"]


# Test case for GET /items/
def test_get_items(db):
    
    item_data1 = {"name": "Item 1", "description": "Description 1", "price": 10.0, "available": True}
    item_data2 = {"name": "Item 2", "description": "Description 2", "price": 15.0, "available": True}

    # Create two items
    client.post("/items/", json=item_data1)
    client.post("/items/", json=item_data2)

    # Retrieve all items
    response = client.get("/items/")
    assert response.status_code == 200
    items = response.json()
    
    # Verify both items are returned
    assert len(items) >= 2
    assert any(item["name"] == item_data1["name"] for item in items)
    assert any(item["name"] == item_data2["name"] for item in items)


    # Test case for GET /items/{item_id}
def test_get_item(db):
    
    item_data = {"name": "Test Item", "description": "Test description", "price": 20.0, "available": True}
    
    # Create the item
    response = client.post("/items/", json=item_data)
    created_item = response.json()
    item_id = created_item["id"]
    
    # Retrieve the created item by ID
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    retrieved_item = response.json()
    
    # Verify the retrieved item matches the created item
    assert retrieved_item["id"] == item_id
    assert retrieved_item["name"] == item_data["name"]
    assert retrieved_item["price"] == item_data["price"]



# Test case for PUT /items/{item_id}
def test_update_item(db):
    
    item_data = {"name": "Test Item", "description": "Test description", "price": 20.0, "available": True}
    
    # Create the item
    response = client.post("/items/", json=item_data)
    created_item = response.json()
    item_id = created_item["id"]
    
    # Update the item
    updated_item_data = {"name": "Updated Item", "description": "Updated description", "price": 25.0, "available": False}
    response = client.put(f"/items/{item_id}", json=updated_item_data)
    assert response.status_code == 200
    updated_item = response.json()
    
    # Verify the item was updated correctly
    assert updated_item["name"] == updated_item_data["name"]
    assert updated_item["price"] == updated_item_data["price"]
    assert updated_item["available"] == updated_item_data["available"]

# Test case for DELETE /items/{item_id}
def test_delete_item(db):
    
    item_data = {"name": "Test Item", "description": "Test description", "price": 20.0, "available": True}
    
    # Create the item
    response = client.post("/items/", json=item_data)
    created_item = response.json()
    item_id = created_item["id"]
    
    # Delete the item
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    delete_message = response.json()
    assert delete_message["message"] == "Item deleted"
    
    # Verify the item no longer exists
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 404  # Item should be gone