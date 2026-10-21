

import json
from pathlib import Path


# Locate the project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Locate customers.json
CUSTOMERS_FILE = (
    PROJECT_ROOT / "data" / "mock_data" / "customers.json"
)


def lookup_customer(customer_id: str) -> dict | None:
    """Find a customer by customer ID."""

    # Load customer records
    with open(CUSTOMERS_FILE, "r", encoding="utf-8") as file:
        customers = json.load(file)

    # Search for the requested customer
    for customer in customers:
        if customer.get("customer_id") == customer_id:
            return customer

    # Customer was not found
    return None
