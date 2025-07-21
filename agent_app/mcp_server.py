# agent_app/mcp_server.py
from fastmcp import FastMCP
from agent_app import tools as ecommerce_tools

# Create the FastMCP server instance
mcp = FastMCP(
    name="Katalyst E-commerce Tool Service"
)

# Register the tool functions from tools.py
mcp.tool()(ecommerce_tools.get_order_status)
mcp.tool()(ecommerce_tools.find_orders_by_customer)
mcp.tool()(ecommerce_tools.cancel_order)

# Start the server when the file is run
if __name__ == "__main__":
    print("🚀 Starting Katalyst FastMCP Tool Server...")
    mcp.run()