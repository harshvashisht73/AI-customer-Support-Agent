
from typing import Annotated, TypedDict

from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    question: str
    context: str
    answer: str
    sources: list[str]
    messages: Annotated[list[AnyMessage], add_messages]