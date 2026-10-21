

from typing import Literal
from pydantic import BaseModel, Field


class SupportTicket(BaseModel):
    ticket_id: str
    customer_id: str | None = None
    issue: str = Field(min_length=5)
    priority: Literal["low", "medium", "high"] = "medium"
    status: Literal["open", "in_progress", "resolved"] = "open"


# python -c "from src.models.support_ticket import SupportTicket; ticket = SupportTicket(ticket_id='TKT-1001', customer_id='CUS1001', issue='Refund pending for 20 days', priority='high'); print(ticket); print(ticket.model_dump())"