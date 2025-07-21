# Katalyst - An AI-Powered E-commerce Agent

This project is a fully containerized, AI-powered agent that can understand natural language requests to manage e-commerce orders.

## Architecture

The system uses a distributed architecture where a `Google ADK Agent` communicates with a custom `MCP Tool Server` to interact with a **PostgreSQL** database. The entire backend is orchestrated using **Docker Compose**.

- **AI Agent:** `google-adk`
- **Tool Server:** `fastmcp`
- **Database:** `PostgreSQL`
- **API:** `FastAPI`
- **Containerization:** `Docker` & `Docker Compose`

## Setup

1.  **Prerequisites:**
    * Docker Desktop
    * Python 3.11+

2.  **Configuration:**
    * Create a `.env` file from the `.env.example` template and add your Google API Key.

3.  **Run the Application:**
    * Run `docker compose up --build -d` to build and start all services.
    * The database will be seeded automatically on the first run.

## How to Test

The agent is exposed via a FastAPI endpoint. You can send `POST` requests to `http://localhost:8000/chat`.

**Example Request:**
```json
{
  "prompt": "What is the status of order A-12345?"
}
```