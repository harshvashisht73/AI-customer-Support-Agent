

import json
from pathlib import Path


# Locate the project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Locate orders.json
ORDERS_FILE = (
    PROJECT_ROOT / "data" / "mock_data" / "orders.json"
)


def lookup_order(order_id: str) -> dict | None:
    """Find an order using its order ID."""

    # Load order records from the JSON file
    with open(ORDERS_FILE, "r", encoding="utf-8") as file:
        orders = json.load(file)

    # Search for the matching order
    for order in orders:
        if order.get("order_id") == order_id:
            return order

    # Return None if the order does not exist
    return None

