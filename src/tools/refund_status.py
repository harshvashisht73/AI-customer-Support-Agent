

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

REFUNDS_FILE = (
    PROJECT_ROOT / "data" / "mock_data" / "refunds.json"
)


def get_refund_status(order_id: str) -> dict | None:
    """Find refund information using an order ID."""

    with open(REFUNDS_FILE, "r", encoding="utf-8") as file:
        refunds = json.load(file)

    for refund in refunds:
        if refund.get("order_id") == order_id:
            return refund

    return None



