


from typing import Literal

from pydantic import BaseModel, Field


class AgentResponse(BaseModel):
    answer: str = Field(min_length=1)
    intent: Literal[
        "general",
        "order_status",
        "refund",
        "cancellation",
        "human_escalation",
    ]
    order_id: str | None = None
    needs_human: bool = False
    priority: Literal["low", "medium", "high"] = "medium"
