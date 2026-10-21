

from src.tools.order_lookup import lookup_order


def test_load_existing_order():
    order = lookup_order("ORD1002")

    assert order is not None
    assert order["order_id"] == "ORD1002"
    assert order["product"] == "Laptop Stand"


def test_nonexistent_order_returns_none():
    order = lookup_order("ORD9999")

    assert order is None
