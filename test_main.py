import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from main import app, get_db
from database import Item

# Create a TestClient instance
client = TestClient(app)

# Mock database session
@pytest.fixture
def mock_db():
    db = MagicMock(spec=Session)
    return db

# Override FastAPI dependency to use mock DB
def override_get_db():
    db = MagicMock(spec=Session)
    yield db

app.dependency_overrides[get_db] = override_get_db

# Sample test item data
test_item = {"name": "Test Item", "description": "A test item", "price": 99.99, "available": True}

# Test: Create Item
def test_create_item(mock_db):
    mock_item = Item(id=1, **test_item)  # Mock database item object
    mock_db.add.return_value = None
    mock_db.commit.return_value = None
    mock_db.refresh.return_value = None

    # Mock the return value of add and refresh
    mock_db.query.return_value.filter.return_value.first.return_value = None

    response = client.post("/items/", json=test_item)

    assert response.status_code == 200
    assert response.json()["name"] == test_item["name"]

# Test: Get All Items
# def test_get_items(mock_db):
#     mock_item = Item(id=1, **test_item)
#     mock_db.query.return_value.all.return_value = [mock_item]

#     response = client.get("/items/")

#     assert response.status_code == 200
#     assert len(response.json()) == 1

# Test: Get Single Item (Existing)
# def test_get_item_existing(mock_db):
#     mock_item = Item(id=1, **test_item)
#     mock_db.query.return_value.filter.return_value.first.return_value = mock_item

#     response = client.get("/items/1")

#     assert response.status_code == 200
#     assert response.json()["name"] == test_item["name"]

# Test: Get Single Item (Non-Existing)
# def test_get_item_non_existing(mock_db):
#     mock_db.query.return_value.filter.return_value.first.return_value = None

#     response = client.get("/items/99")

#     assert response.status_code == 404
#     assert response.json()["detail"] == "Item not found"

# Test: Update Item
# def test_update_item(mock_db):
#     mock_item = Item(id=1, **test_item)
#     mock_db.query.return_value.filter.return_value.first.return_value = mock_item

#     updated_item = {"name": "Updated Item", "description": "Updated description", "price": 199.99, "available": False}
#     response = client.put("/items/1", json=updated_item)

#     assert response.status_code == 200
#     assert response.json()["name"] == "Updated Item"

# Test: Delete Item
def test_delete_item(mock_db):
    mock_item = Item(id=1, **test_item)
    mock_db.query.return_value.filter.return_value.first.return_value = mock_item

    response = client.delete("/items/1")

    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted"
