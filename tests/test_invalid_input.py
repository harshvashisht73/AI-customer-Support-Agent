

from src.agents.agent import answer_with_agent


def test_empty_question_is_rejected():
    result = answer_with_agent("")

    assert result["answer"] == (
        "Please enter a valid, non-empty question."
    )
    assert result["sources"] == []


def test_whitespace_question_is_rejected():
    result = answer_with_agent("   ")

    assert result["answer"] == (
        "Please enter a valid, non-empty question."
    )
    assert result["sources"] == []


def test_none_question_is_rejected():
    result = answer_with_agent(None)

    assert result["answer"] == (
        "Please enter a valid, non-empty question."
    )
    assert result["sources"] == []
