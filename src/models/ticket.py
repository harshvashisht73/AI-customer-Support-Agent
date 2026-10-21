

from pydantic import BaseModel
from typing import Literal


class SupportTicket(BaseModel):
    ticket_id: str
    customer_id: str
    issue: str
    priority: Literal["low", "medium", "high"]
    status: Literal["open", "in_progress", "resolved"] = "open"


if __name__ == "__main__":
    ticket = SupportTicket(
        ticket_id="TKT1001",
        customer_id="CUS1001",
        issue="Refund has not arrived",
        priority="high"
    )

    print(ticket)
    print(ticket.model_dump())