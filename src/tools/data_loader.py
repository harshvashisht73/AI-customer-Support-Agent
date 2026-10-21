

import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "mock_data"


def load_json(filename: str):
    file_path = DATA_DIR / filename

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    customers = load_json("customers.json")
    orders = load_json("orders.json")
    refunds = load_json("refunds.json")

    print("Customers loaded:", len(customers))
    print("Orders loaded:", len(orders))
    print("Refunds loaded:", len(refunds))

    print("\nFirst customer:")
    print(customers[0])



# print("Full file path:", Path(__file__).resolve())
# print("Parent 0:", Path(__file__).resolve().parents[0])
# print("Parent 1:", Path(__file__).resolve().parents[1])
# print("Parent 2:", Path(__file__).resolve().parents[2])
# print("Project root:", PROJECT_ROOT)

