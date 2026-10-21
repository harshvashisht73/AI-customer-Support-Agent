
from pydantic import BaseModel, Field
from typing import Literal

class Order(BaseModel):
    order_id: str
    customer_id: str
    status: Literal[
            "processing",
            "shipped",
            "delivered",
            "cancelled"
    ]
    total_amount: float = Field(ge=0)



if __name__ == "__main__":
    order = Order(
        order_id="ORD1001",
        customer_id="CUS1001",
        status="shipped",
        total_amount=1499.0
    )

    print(order)
    print(order.model_dump())

