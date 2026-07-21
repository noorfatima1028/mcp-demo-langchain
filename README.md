# MCP with LangChain & LangGraph

This repository demonstrates my hands-on learning of the **Model Context Protocol (MCP)** using **LangChain**, **LangGraph**, and **Groq LLMs**. The project showcases how AI agents can discover and invoke external tools through MCP servers using both **STDIO** and **Streamable HTTP** transports.

---

## 🚀 Features

- Built a Math MCP Server using FastMCP
- Built a Weather MCP Server using FastMCP
- Exposed custom tools using the `@mcp.tool()` decorator
- Implemented both **STDIO** and **Streamable HTTP** transports
- Connected multiple MCP servers using `MultiServerMCPClient`
- Integrated Groq Llama 3.3 70B with LangChain
- Built a ReAct Agent using LangGraph
- Enabled dynamic tool discovery from MCP servers
- Executed external tools through natural language prompts
- Managed API keys securely using environment variables

---

## 🛠️ Tech Stack

- Python
- MCP (Model Context Protocol)
- FastMCP
- LangChain
- LangGraph
- Groq (Llama 3.3 70B Versatile)
- python-dotenv

---

## 📂 Repository Structure

```text
.
├── client.py
├── main.py
├── mathserver.py
├── weather.py
├── pyproject.toml
├── requirements.txt
├── README.md
└── uv.lock
```

---

## 📚 Concepts Covered

### MCP (Model Context Protocol)

- MCP Fundamentals
- MCP Server
- MCP Client
- Tool Discovery
- Tool Registration
- STDIO Transport
- Streamable HTTP Transport

### LangChain

- Chat Models
- LLM Integration
- Prompt Engineering

### LangGraph

- ReAct Agent Architecture
- Tool Calling
- Agent Workflows

---

## ⚙️ Getting Started

### Clone the repository

```bash
git clone <repository-url>
cd <repository-name>
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Running the Project

### Start the Weather MCP Server

```bash
python weather.py
```

### Run the Client

Open another terminal and run:

```bash
python client.py
```

The Math MCP Server is automatically started by the client through the `MultiServerMCPClient`.

---

## 🎯 Learning Objectives

This project helped me understand:

- Building MCP servers with FastMCP
- Creating custom AI tools
- Connecting multiple MCP servers
- Tool discovery using MCP
- LangChain integration with Groq
- Building ReAct Agents with LangGraph
- Communication between AI agents and external tools

---

## 🚧 Future Improvements

- File System MCP Server
- Database MCP Server
- GitHub MCP Integration
- Multi-Agent Systems
- Retrieval-Augmented Generation (RAG)
- Model Context Protocol Authentication
- Production-ready MCP Applications

---

## 👩‍💻 Author

**Noor Fatima**

Aspiring Python | FastAPI | AWS | Agentic AI Developer