import pytest

from src.webshop.shopping_cart import ShoppingCart
from src.webshop.database import Database
from src.webshop.item import Item


@pytest.fixture
def seeds():
    return Item("Blandade fröer", 25)

@pytest.fixture
def empty_cart(seeds):
    return ShoppingCart()

@pytest.fixture
def db(mocker):
    mock_db = mocker.Mock(spec=Database)
    mock_db.add_item_to_cart.return_value = None
    return mock_db

@pytest.fixture
def cart(db):
    c = ShoppingCart()
    c.set_database(db)
    c.add_item("Spade", 50)
    return c

@pytest.fixture
def db(mocker):
    mock_db = mocker.Mock(spec=Database)
    mock_db.add_item_to_cart.return_value = None
    return mock_db


def test_add_item_to_empty_cart(mocker, seeds, empty_cart):
    #Arrange
    mock_database = mocker.Mock(spec=Database)
    mock_database.add_item_to_cart.return_value = None
    empty_cart.set_database(mock_database)

    #Act
    empty_cart.add_item(seeds.name, seeds.price)

    #Assert
    mock_database.add_item_to_cart.assert_called_once()
    mock_database.add_item_to_cart.asser_called_with(seeds.name, seeds.price)

def test_add_item_to_cart(mocker, db, seeds, cart):
    cart.set_database(db)

    expected_call_count = 1 + 1


    cart.add_item(seeds.name, seeds.price)


    actual_call_count = db.add_item_to_cart.call_count

    assert actual_call_count == expected_call_count
    db.add_item_to_cart.asser_called_with(seeds.name, seeds.price)