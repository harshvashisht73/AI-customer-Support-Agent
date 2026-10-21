

from pydantic import ValidationError
from src.models.agent_response import AgentResponse

# Test 1: Valid response
valid_data = {
    "answer": "Your order is processing.",
    "intent": "order_status",
    "order_id": "ORD1002",
    "needs_human": False,
    "priority": "medium",
}

response = AgentResponse.model_validate(valid_data)
print("VALID RESPONSE:", response.model_dump())

# Test 2: Invalid intent
invalid_data = {
    "answer": "Your order is processing.",
    "intent": "track_package",
    "order_id": "ORD1002",
    "needs_human": False,
    "priority": "medium",
}

try:
    AgentResponse.model_validate(invalid_data)
except ValidationError as error:
    print("\nVALIDATION FAILED:")
    print(error)



# Test 3: Incomplete response
incomplete_data = {
    "answer": "",
    "intent": "order_status",
}

try:
    response = AgentResponse.model_validate(incomplete_data)
    print("\nINCOMPLETE RESPONSE ACCEPTED:", response.model_dump())

except ValidationError as error:
    print("\nINCOMPLETE RESPONSE REJECTED:")
    print(error)


# Test 4: Recover from an invalid response
incomplete_data = {
    "answer": "",
    "intent": "order_status",
}

try:
    response = AgentResponse.model_validate(incomplete_data)

except ValidationError as error:
    print("\nVALIDATION ERROR CAUGHT:", error.errors())

    # Safe fallback response
    response = AgentResponse(
        answer="I'm sorry, I couldn't prepare a reliable answer. Please try again.",
        intent="general",
    )

print("\nFINAL RESPONSE AFTER RECOVERY:")
print(response.model_dump())
