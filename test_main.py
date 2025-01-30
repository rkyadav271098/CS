from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

# Sample item to use in tests
test_item = {
    "name": "Test Item",
    "description": "This is a test item",
    "price": 100.0,
    "available": True
}

def test_create_item():
    """Test creating a new item"""
    response = client.post("/items/", json=test_item)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_item["name"]
    assert data["description"] == test_item["description"]
    assert data["price"] == test_item["price"]
    assert data["available"] == test_item["available"]
    assert "id" in data  # ID should be auto-generated
    global item_id
    item_id = data["id"]  # Store ID for future tests

def test_get_all_items():
    """Test retrieving all items"""
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(item["name"] == test_item["name"] for item in data)

def test_get_specific_item():
    """Test retrieving a specific item"""
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_item["name"]

def test_update_item():
    """Test updating an existing item"""
    updated_item = {
        "name": "Updated Item",
        "description": "Updated description",
        "price": 150.0,
        "available": False
    }
    response = client.put(f"/items/{item_id}", json=updated_item)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == updated_item["name"]
    assert data["description"] == updated_item["description"]
    assert data["price"] == updated_item["price"]
    assert data["available"] == updated_item["available"]

def test_delete_item():
    """Test deleting an item"""
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted"}

def test_get_deleted_item():
    """Test retrieving a deleted item (should return 404)"""
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
