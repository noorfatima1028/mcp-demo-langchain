import asyncio
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


async def main():
    # Create MCP Client
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],  # Ensure this file exists
                "transport": "stdio",
            },
            "weather": {
    "url": "http://127.0.0.1:8000/mcp",
    "transport": "streamable_http",
},
        }
    )

    # Get available tools from MCP servers
    tools = await client.get_tools()

    # Initialize Groq model
    model = ChatGroq(
        model="llama-3.3-70b-versatile"
    )

    # Create ReAct Agent
    agent = create_react_agent(
        model=model,
        tools=tools,
    )

    # Invoke the agent
    math_response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What's (3 + 5) * 12?",
                }
            ]
        }
    )

    print("Math Response:", math_response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())