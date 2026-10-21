

from uuid import uuid4

from src.models.support_ticket import SupportTicket


def create_support_ticket(
    issue: str,
    customer_id: str | None = None,
    priority: str = "medium",
) -> dict:
    ticket = SupportTicket(
        ticket_id=f"TKT-{uuid4().hex[:8].upper()}",
        customer_id=customer_id,
        issue=issue,
        priority=priority,
        status="open",
    )

    return ticket.model_dump()
