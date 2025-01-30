from fastapi.testclient import TestClient
from main import app
import pytest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from main import get_item, create_item, update_item, delete_item
from database import Item
from main import ItemSchema

client = TestClient(app)

# Sample item to use in tests
test_item = {
    "name": "Test Item",
    "description": "This is a test item",
    "price": 100.0,
    "available": True
}

@pytest.fixture
def mock_db():
    """Fixture to create a mock database session"""
    return MagicMock(spec=Session)

def test_create_item(mock_db):
    """Test creating a new item"""
    item_data = ItemSchema(name="Test Item", description="A test", price=100.0, available=True)
    mock_item = Item(id=1, **item_data.dict())
    
    mock_db.add = MagicMock()
    mock_db.commit = MagicMock()
    mock_db.refresh = MagicMock()

    result = create_item(item_data, mock_db)

    assert result.name == item_data.name
    assert result.price == item_data.price
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()

# def test_get_all_items(mock_db):
#     """Test retrieving all items"""
#     mock_items = [Item(id=1, name="Test Item", description="A test", price=100.0, available=True)]
#     mock_db.query.return_value.all.return_value = mock_items

#     response = client.get("/items/")
#     assert response.status_code == 200
#     data = response.json()
#     assert isinstance(data, list)
#     assert any(item["name"] == "Test Item" for item in data)

def test_get_specific_item(mock_db):
    """Test retrieving a specific item"""
    mock_item = Item(id=1, name="Test Item", description="A test", price=100.0, available=True)
    mock_db.query.return_value.filter.return_value.first.return_value = mock_item

    result = get_item(1, mock_db)
    
    assert result.id == 1
    assert result.name == "Test Item"

def test_update_item(mock_db):
    """Test updating an existing item"""
    mock_item = Item(id=1, name="Old Name", description="Old Desc", price=50.0, available=True)
    updated_data = ItemSchema(name="Updated Item", description="New Desc", price=150.0, available=False)

    mock_db.query.return_value.filter.return_value.first.return_value = mock_item

    result = update_item(1, updated_data, mock_db)

    assert result.name == updated_data.name
    assert result.description == updated_data.description
    assert result.price == updated_data.price

def test_delete_item(mock_db):
    """Test deleting an existing item"""
    mock_item = Item(id=1, name="Test Item", description="A test", price=100.0, available=True)
    
    mock_db.query.return_value.filter.return_value.first.return_value = mock_item
    mock_db.delete = MagicMock()
    mock_db.commit = MagicMock()

    result = delete_item(1, mock_db)

    assert result == {"message": "Item deleted"}
    mock_db.delete.assert_called_once_with(mock_item)
    mock_db.commit.assert_called_once()

def test_get_deleted_item(mock_db):
    """Test retrieving a deleted item (should return 404)"""
    mock_db.query.return_value.filter.return_value.first.return_value = None

    response = client.get(f"/items/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
