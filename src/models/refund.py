

from pydantic import BaseModel, Field
from typing import Literal


class Refund(BaseModel):
    refund_id: str
    order_id: str
    customer_id: str
    amount: float = Field(ge=0)
    status: Literal[
        "pending",
        "approved",
        "processed",
        "rejected"
    ]


if __name__ == "__main__":
    refund = Refund(
        refund_id="REF1001",
        order_id="ORD1001",
        customer_id="CUS1001",
        amount=499.0,
        status="processed"
    )

    print(refund)
    print(refund.model_dump())