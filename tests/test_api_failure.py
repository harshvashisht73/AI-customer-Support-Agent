

from unittest.mock import patch

from src.agents.agent import answer_with_agent


def test_agent_handles_api_failure():
    with patch(
        "src.agents.agent.workflow.invoke",
        side_effect=RuntimeError("Simulated API failure"),
    ):
        result = answer_with_agent(
            "What is the status of order ORD1002?",
            thread_id="test-api-failure-001",
        )

    assert result["answer"] == (
        "Sorry, our support service is temporarily unavailable. "
        "Please try again later."
    )
    assert result["sources"] == []
