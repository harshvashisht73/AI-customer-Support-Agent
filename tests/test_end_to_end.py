

from unittest.mock import patch

from src.agents.agent import answer_with_agent


def test_order_status_workflow():
    result = answer_with_agent(
        "What is the status of order ORD1002?",
        thread_id="e2e-order-status",
    )

    assert isinstance(result, dict)
    assert result["answer"].strip()
    assert "processing" in result["answer"].lower()


def test_unknown_order_does_not_crash():
    result = answer_with_agent(
        "What is the status of order ORD9999?",
        thread_id="e2e-unknown-order",
    )

    assert isinstance(result, dict)
    assert isinstance(result["answer"], str)
    assert result["answer"].strip()


def test_invalid_input_is_handled():
    result = answer_with_agent(
        "   ",
        thread_id="e2e-invalid-input",
    )

    assert result["answer"] == (
        "Please enter a valid, non-empty question."
    )
    assert result["sources"] == []


def test_api_failure_is_handled():
    with patch(
        "src.agents.agent.workflow.invoke",
        side_effect=RuntimeError("Simulated API failure"),
    ):
        result = answer_with_agent(
            "What is the status of order ORD1002?",
            thread_id="e2e-api-failure",
        )

    assert result["answer"] == (
        "Sorry, our support service is temporarily unavailable. "
        "Please try again later."
    )
    assert result["sources"] == []
