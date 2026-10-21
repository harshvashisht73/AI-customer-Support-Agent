

from src.agents.agent import answer_with_agent


def test_agent_answers_order_status_question():
    result = answer_with_agent(
        "What is the status of order ORD1002?",
        thread_id="test-order-status-001",
    )

    assert isinstance(result, dict)
    assert "answer" in result
    assert isinstance(result["answer"], str)
    assert result["answer"].strip() != ""

    # The agent should use the order lookup tool.
    assert "processing" in result["answer"].lower()


def test_agent_returns_sources_field():
    result = answer_with_agent(
        "Hello, how can you help me?",
        thread_id="test-general-question-001",
    )

    assert "sources" in result
    assert isinstance(result["sources"], list)
