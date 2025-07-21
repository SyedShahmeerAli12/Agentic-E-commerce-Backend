# agent_app/agent.py
import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from google.adk.models import Gemini
from dotenv import load_dotenv

load_dotenv()

katalyst_agent = LlmAgent(
    name="katalyst_ecommerce_agent",
    description="An agent that can answer questions about e-commerce orders.",
    model=Gemini(
        model_name="gemini-1.5-flash",
        api_key=os.getenv("GOOGLE_API_KEY")
    ),
    tools=[
        MCPToolset(connection_params=StdioServerParameters(
            command='python',
            args=['-m', 'agent_app.mcp_server']
        ))
    ],
)