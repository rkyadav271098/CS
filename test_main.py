import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from main import app, get_db, Item

# Mock database session
def override_get_db():
    db = MagicMock(spec=Session)
    yield db

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# Sample test data
test_item = {
    "name": "Test Item",
    "description": "This is a test item",
    "price": 10.99,
    "available": True
}

def test_create_item():
    response = client.post("/items/", json=test_item)
    assert response.status_code == 200
    assert response.json()["name"] == test_item["name"]

def test_get_items():
    response = client.get("/items/")
    assert response.status_code == 200

# def test_get_item():
#     item_id = 1
#     response = client.get(f"/items/{item_id}")
#     if response.status_code == 404:
#         assert response.json()["detail"] == "Item not found"
#     else:
#         assert response.status_code == 200
#         assert response.json()["id"] == item_id

# def test_update_item():
#     item_id = 1
#     updated_item = test_item.copy()
#     updated_item["price"] = 15.99
#     response = client.put(f"/items/{item_id}", json=updated_item)
#     if response.status_code == 404:
#         assert response.json()["detail"] == "Item not found"
#     else:
#         assert response.status_code == 200
#         assert response.json()["price"] == updated_item["price"]

# def test_delete_item():
#     item_id = 1
#     response = client.delete(f"/items/{item_id}")
#     if response.status_code == 404:
#         assert response.json()["detail"] == "Item not found"
#     else:
#         assert response.status_code == 200
#         assert response.json()["message"] == "Item deleted"
