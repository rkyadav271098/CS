import pytest
from unittest.mock import MagicMock
from fastapi import HTTPException
from sqlalchemy.orm import Session
from main import get_item, create_item, update_item, delete_item
from database import Item
from main import ItemSchema

@pytest.fixture
def mock_db():
    """Fixture to create a mock database session"""
    return MagicMock(spec=Session)

# Override the 'get_db' dependency with a mock version
@pytest.fixture(autouse=True)
def mock_get_db(monkeypatch, mock_db):
    """Monkeypatch the get_db dependency to return the mocked session"""
    monkeypatch.setattr("main.get_db", lambda: mock_db)

def test_create_item(mock_db):
    """Test creating an item"""
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

def test_get_item_found(mock_db):
    """Test retrieving an existing item"""
    mock_item = Item(id=1, name="Test Item", description="A test", price=100.0, available=True)
    mock_db.query.return_value.filter.return_value.first.return_value = mock_item

    result = get_item(1, mock_db)
    
    assert result.id == 1
    assert result.name == "Test Item"

def test_get_item_not_found(mock_db):
    """Test retrieving a non-existent item"""
    mock_db.query.return_value.filter.return_value.first.return_value = None

    with pytest.raises(HTTPException) as exc:
        get_item(99, mock_db)

    assert exc.value.status_code == 404
    assert exc.value.detail == "Item not found"

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

# def test_get_deleted_item(mock_db):
#     """Test retrieving a deleted item (should return 404)"""
#     mock_db.query.return_value.filter.return_value.first.return_value = None

#     result = get_item(99, mock_db)

#     assert result is None
