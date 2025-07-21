# Katalyst: An AI-Powered E-commerce Agent

Katalyst is a fully containerized, AI-powered agent designed to automate e-commerce order management. It understands natural language requests, selects the appropriate tool, and interacts with a PostgreSQL database to perform actions like checking order statuses or canceling orders.

This project demonstrates a complete, multi-component backend system built with modern development practices.

## Key Features

* **🤖 Agentic System:** Uses the Google ADK framework to create a true AI agent that makes decisions, not just a simple chatbot.
* **🛠️ Tool-Based Actions:** The agent uses a set of predefined tools (hosted in a separate MCP Server process) to interact with the system's database in real-time.
* **📦 Fully Containerized:** The entire application stack (Agent, Database, MCP Server) is managed by Docker and Docker Compose for a one-command setup.
* **🔗 API-Driven:** Exposes a simple and clean FastAPI endpoint for interaction.
* **⚙️ Automated Setup:** Includes an automated database seeding service that populates the database on the first run.

## Tech Stack

* **Backend:** Python, FastAPI
* **AI Framework:** Google ADK (Agent Development Kit)
* **LLM:** Google Gemini (via API)
* **Database:** PostgreSQL
* **Containerization:** Docker & Docker Compose

## Architecture

The system uses a decoupled architecture. A FastAPI server runs the main ADK Agent. When the agent needs to perform an action, it starts and communicates with a separate MCP Tool Server as a subprocess. This server then executes the required database operations against the PostgreSQL database. This entire process is orchestrated within Docker.

## Getting Started

### Prerequisites
* Git
* Docker Desktop (must be running)

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/katalyst-agent.git](https://github.com/your-username/katalyst-agent.git)
```
```bash
cd katalyst-agent
```


### 2. Configure Environment
Create a `.env` file for your secret API key by copying the template.

* On Windows:
    ```bash
    copy .env.example .env
    ```
* On Mac/Linux:
    ```bash
    cp .env.example .env
    ```
Now, open the new `.env` file and add your Google API Key.

### 3. Build and Run
This single command will build the Docker images, start the database, automatically seed it with sample data, and start the agent's API server.

```bash
docker compose up --build -d
```
The system is now running.

## How to Use the Agent

The agent is available via a POST request to the API.

* **Endpoint:** `POST http://localhost:8000/chat`
* **Body:** (raw, JSON)
    ```json
    {
      "prompt": "Your request to the agent"
    }
    ```

### Example Requests

#### Check Order Status
```json
{
  "prompt": "What is the status of order A-12345?"
}
```

#### Find a Customer's Orders
```json
{
  "prompt": "Find all orders for alice@example.com"
}
```

#### Cancel a Pending Order
```json
{
  "prompt": "Please cancel order B-54321"
}
```

## How to Stop

To stop all the running containers, run:
```bash
docker compose down
```
