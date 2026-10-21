
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool
from langchain_core.messages import SystemMessage
from src.agents.llm import get_llm
from langchain_core.messages import SystemMessage
from src.state.agent_state import AgentState
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from src.tools.escalation import create_support_ticket
from langchain_core.tools import tool
from src.retrieval.retriever import get_retriever



from src.tools.customer_lookup import lookup_customer
from src.tools.order_lookup import lookup_order
from src.tools.refund_status import get_refund_status
from src.tools.eligibility_checks import (
    check_cancellation_eligibility,
    check_refund_eligibility,
)



conversation_messages = []




@tool
def customer_lookup_tool(customer_id: str) -> dict | None:
    """Look up customer details using a customer ID."""
    return lookup_customer(customer_id)


@tool
def order_lookup_tool(order_id: str) -> dict | None:
    """Look up order details using an order ID."""
    return lookup_order(order_id)


@tool
def refund_status_tool(order_id: str) -> dict | None:
    """Find the refund status for an order ID."""
    return get_refund_status(order_id)


@tool
def cancellation_eligibility_tool(order_id: str) -> dict:
    """Check whether an order can be requested for cancellation."""
    return check_cancellation_eligibility(order_id)


@tool
def refund_eligibility_tool(order_id: str) -> dict:
    """Check the recorded refund status and eligibility for an order."""
    return check_refund_eligibility(order_id)

@tool
def escalate_to_human(
    issue: str,
    customer_id: str | None = None,
    priority: str = "medium",
) -> dict:
    """Create a support ticket when a customer needs human assistance."""
    return create_support_ticket(
        issue=issue,
        customer_id=customer_id,
        priority=priority,
    )



@tool
def search_knowledge_base(question: str) -> str:
    """Search ShopEase policies, FAQs, delivery information,
    return rules, and other knowledge-base documents."""

    retriever = get_retriever()
    documents = retriever.invoke(question)

    if not documents:
        return "No relevant information was found in the knowledge base."

    results = []
    sources = []

    for document in documents:
        source = document.metadata.get("source", "Unknown")

        if source != "Unknown" and source not in sources:
            sources.append(source)

        results.append(
            f"Source: {source}\n"
            f"Content: {document.page_content}"
        )

    # Store retrieved sources for the current agent request.
    conversation_sources[thread_context["thread_id"]] = sources

    return "\n\n".join(results)




tools = [
    search_knowledge_base,
    customer_lookup_tool,
    order_lookup_tool,
    refund_status_tool,
    cancellation_eligibility_tool,
    refund_eligibility_tool,
    escalate_to_human

]

llm = get_llm()
llm_with_tools = llm.bind_tools(tools)


from langchain_core.messages import SystemMessage



def agent_node(state: AgentState) -> dict:
    response = llm_with_tools.invoke(
        [
            SystemMessage(
        content=(
        
        "You are ShopEase customer support. "
        "Use tools to look up customer, order, refund, and eligibility information. "
        "Never invent customer or order details. "
        '''Use search_knowledge_base for questions about ShopEase policies,
        FAQs, return rules, delivery policies, and general support information.

        Use order and refund tools for customer-specific order or refund data.

        Do not invent policy details when the knowledge base does not provide
        relevant information. Tell the customer when the available information
        is insufficient.'''

        "ESCALATION RULES: "
        "If a customer explicitly asks for a human, human representative, "
        "or real person, you MUST call escalate_to_human in the current turn. "
        "If a customer reports repeated unsuccessful attempts to resolve an issue, "
        "or a serious unresolved complaint, you MUST call escalate_to_human "
        "in the current turn. "
        "Do not delay either escalation by asking for an order number or email. "
        "The customer ID is optional; if unknown, pass None. "
        "Use the customer's message to describe the issue. "
        "Use high priority for serious or urgent unresolved complaints; "
        "otherwise use medium priority. "

        "After the tool returns, provide the ticket ID and status. "
        "Do not claim a human has been notified, has reviewed the ticket, "
        "or will contact the customer unless the system confirms that action. "
        "Never claim to perform actions your tools do not support."

    )

            ),
            *state["messages"],
        ]
    )
    print("LLM tool calls:", response.tool_calls)
    return {"messages": [response]}


graph = StateGraph(AgentState)

graph.add_node("agent", agent_node)
graph.add_node("tools", ToolNode(tools))

graph.add_edge(START, "agent")

graph.add_conditional_edges(
    "agent",
    tools_condition,
)

graph.add_edge("tools", "agent")



memory = InMemorySaver()

workflow = graph.compile(checkpointer=memory)



conversation_messages = []



def answer_with_agent(
    question: str,
    thread_id: str = "shopease-session-1",
) -> dict:

    # Validate customer input before calling the LLM
    if not isinstance(question, str) or not question.strip():
        return {
            "answer": "Please enter a valid, non-empty question.",
            "sources": [],
        }

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    
    try:
        result = workflow.invoke(
        {
            "question": question,
            "context": "",
            "answer": "",
            "sources": [],
            "messages": [
                {
                    "role": "user",
                    "content": question,
                }
            ],
        },
            config=config,
    )

    except Exception:
        return {
        "answer": (
            "Sorry, our support service is temporarily unavailable. "
            "Please try again later."
        ),
        "sources": [],
    }



    
    last_message = result["messages"][-1]

    return {
        "answer": last_message.content,
        "sources": result["sources"],
    }



