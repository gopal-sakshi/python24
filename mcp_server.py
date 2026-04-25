from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("TechnicianTools")

@mcp.tool()
def get_breaker_status(breaker_id: str) -> str:
    """Check if a specific electrical breaker is ON or OFF."""
    # In a real scenario, this would talk to actual hardware
    statuses = {"A1": "OFF - Tripped", "B2": "ON - Normal"}
    return statuses.get(breaker_id.upper(), "Unknown Breaker ID")

if __name__ == "__main__":
    mcp.run()