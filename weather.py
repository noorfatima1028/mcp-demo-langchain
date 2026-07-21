from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MATH")


@mcp.tool()
async def get_weather(location: str) -> str:
    """Get the weather for a location."""
    return "It's always raining in California."


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
