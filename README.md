
# ShopEase AI Customer Support Agent

An AI-powered customer support assistant built with Python, LangChain, LangGraph, and retrieval-augmented generation (RAG). This project demonstrates LLM tool calling, knowledge-base retrieval, conversation memory, human escalation, and automated testing in an interactive command-line application.

## Features

- **RAG-based knowledge retrieval:** Search ShopEase policies, FAQs, return rules, and delivery information.
- **Order lookup:** Retrieve order information using an order ID.
- **Refund support:** Check refund status and eligibility.
- **Cancellation checks:** Evaluate cancellation eligibility.
- **LLM tool calling:** Let the agent select appropriate support tools based on customer questions.
- **Conversation memory:** Maintain context across follow-up questions during a session.
- **Human escalation:** Create structured support tickets for issues requiring human assistance.
- **Structured output validation:** Validate response fields using Pydantic.
- **Input validation and error handling:** Handle empty questions and simulated agent/API failures.
- **Automated testing:** Test retrieval, tools, agent workflows, and error handling.

## Technology Stack

- Python
- LangChain
- LangGraph
- Groq-hosted language model
- Chroma vector database
- Hugging Face sentence-transformer embeddings
- Pydantic
- Pytest

## Architecture

```text
Customer
   |
   v
Command-Line Interface
(main.py)
   |
   v
LangGraph Agent
   |
   +----> Knowledge-Base Search Tool
   |           |
   |           v
   |       Chroma Vector Store
   |
   +----> Customer Lookup
   |
   +----> Order Lookup
   |
   +----> Refund Status
   |
   +----> Eligibility Checks
   |
   +----> Human Escalation
   |
   v
Response to Customer
```

The agent can use knowledge-base retrieval for policy questions and business tools for customer-specific requests.

## Project Structure

```text
customer-support-agent/
├── data/
│   ├── documents/
│   ├── mock_data/
│   └── chroma_db/
├── src/
│   ├── agents/
│   ├── config/
│   ├── ingestion/
│   ├── models/
│   ├── prompts/
│   ├── retrieval/
│   ├── state/
│   └── tools/
├── tests/
├── .env
├── requirements.txt
├── main.py
└── README.md
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd customer-support-agent
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a local `.env` file using the variable names expected by your project configuration. Add your own Groq API key.

Never commit `.env` or API keys to GitHub.

### 5. Run the application

```bash
python main.py
```

## Example Questions

- What is the ShopEase refund policy?
- What is the status of order ORD1002?
- Can I cancel order ORD1002?
- What is the status of my refund?
- I need to speak to a human.

Actual answers depend on the knowledge-base content, mock data, and model behavior.

## Running Tests

Run the complete test suite:

```bash
python -m pytest -v
```

Run the end-to-end tests:

```bash
python -m pytest tests/test_end_to_end.py -v
```

The project includes tests for data loading, RAG retrieval, agent workflows, invalid input, and simulated API failures.

## Current Limitations

- Uses mock customer, order, and refund data.
- Conversation memory is stored in memory and does not persist across application restarts.
- Source filenames are not yet returned reliably in the agent's final response.
- Human escalation creates a support ticket but does not automatically notify a real support team.
- Structured output validation has been tested separately and is not yet fully integrated into the main agent workflow.
- The project runs as a command-line application and is not a deployed web service.

## Future Improvements

- Add reliable source tracking to RAG responses.
- Persist support tickets and conversation history.
- Integrate real order-management and customer-management systems.
- Integrate structured response validation into the main workflow.
- Improve logging, retry behavior, and monitoring.
- Add a user interface if needed for deployment.

## Author

Built as an AI engineering portfolio project to demonstrate practical skills in Python, LLM applications, RAG, agentic workflows, tool calling, state management, and testing.
