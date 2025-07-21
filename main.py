# main.py (Definitive Final Version)
from fastapi import FastAPI
from pydantic import BaseModel
from agent_app.agent_core import katalyst_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types as genai_types

app = FastAPI(title="Katalyst Agent API")

session_service = InMemorySessionService()
runner = Runner(
    agent=katalyst_agent,
    app_name="katalyst_agent_app",
    session_service=session_service,
)

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat_with_agent(request: ChatRequest):
    """Sends a prompt to the agent and gets a response."""
    print(f"Received prompt: {request.prompt}")

    session = await session_service.create_session(
        app_name="katalyst_agent_app", user_id="api_user"
    )

    # Correctly construct the message object, as in your example
    user_message = genai_types.Content(
        role="user", parts=[genai_types.Part(text=request.prompt)]
    )

    final_response = "[Agent did not produce a final response]"
    
    async for event in runner.run_async(
        user_id=session.user_id,
        session_id=session.id,
        new_message=user_message,
    ):
        if event.is_final_response() and event.content and event.content.parts:
            final_response = event.content.parts[0].text
            break
            
    print(f"Agent response: {final_response}")
    return {"response": final_response}