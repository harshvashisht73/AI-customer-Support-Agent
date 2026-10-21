
from src.agents.llm import get_llm
from src.models.agent_response import AgentResponse

llm = get_llm()

structured_llm = llm.with_structured_output(AgentResponse)

response = structured_llm.invoke(
    "A customer asks for the status of order ORD1002. "
    "The order is processing. Return the appropriate response."
)

print(response)
print(response.model_dump())