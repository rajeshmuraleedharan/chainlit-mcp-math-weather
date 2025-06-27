# Chainlit with AWS Strands Agents and FastMCP

A demonstration of AWS Strands Agents orchestrating FastMCP servers through a Chainlit interface to perform math calculations and retrieve weather information.

## Overview

This project showcases a Chainlit chat application powered by LLMs (Llama-3) that can:
- Perform math calculations 
- Provide weather information for cities

The application uses AWS Strands Agents to orchestrate Model Context Protocol (MCP) servers as tools, extending the capabilities of the language model.

## Features

- 🧮 **Math Operations**: Addition, subtraction, multiplication, and division
- 🌤️ **Weather Information**: Get simulated weather data for cities
- 💬 **Interactive Chat Interface**: User-friendly Chainlit UI

## Architecture

- **Chainlit**: Provides the chat interface
- **AWS Strands Agents**: Powerful agent framework for orchestrating tools and models
- **FastMCP Servers**: Advanced MCP servers for math and weather capabilities
- **Llama-3**: Language model for natural language understanding
- **AWS Bedrock**: Managed service for foundation models

## Prerequisites

- Python 3.9+
- AWS Bedrock access (configured with proper credentials)
- FastMCP library (`pip install fastmcp`)
- AWS Strands Agents packages (`pip install strands-agents strands-agents-tools strands-agents-builder`)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/chainlit-mcp-math-weather.git
cd chainlit-mcp-math-weather
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Starting the MCP Servers

The MCP servers are automatically started when you run the Chainlit application. 
The application uses subprocess to launch the math and weather MCP servers as needed.

If you want to test the MCP servers individually:

1. **Math MCP Server**:
   ```bash
   python mcp_servers/math_mcp_server.py
   ```

2. **Weather MCP Server**:
   ```bash
   python mcp_servers/weather_mcp_server.py
   ```

### Running the Chainlit Application

Run the Chainlit application:
```bash
chainlit run chainlit_app.py
```

This will start a web server, typically at http://localhost:8000, where you can interact with the assistant.

## Example Prompts

- "What is 42 + 18?"
- "Calculate 15 * 7"
- "Divide 100 by 5"
- "What's the weather in Austin?"
- "Tell me the weather in New York"

## Project Structure

```
├── chainlit_app.py         # Main Chainlit application
├── chainlit.md             # Chainlit configuration
├── main.py                 # Basic entry point script 
├── requirements.txt        # Python dependencies
├── mcp_servers/
│   ├── math_mcp_server.py  # Math operations MCP server
│   └── weather_mcp_server.py # Weather information MCP server
```

## MCP Servers

This project uses [FastMCP](https://gofastmcp.com/) to create Model Context Protocol (MCP) servers that extend the capabilities of the language model.

### Math Server
The math server (`math_mcp_server.py`) provides basic arithmetic operations:
- Addition
- Multiplication
- Subtraction
- Division

### Weather Server
The weather server (`weather_mcp_server.py`) simulates weather information:
- Currently supports Austin and New York 
- Returns simulated temperature and conditions
- Uses Pydantic models for input validation

## AWS Strands Agents

This project leverages AWS Strands Agents, a powerful framework for building AI applications with reasoning and tool-calling capabilities. Key features of AWS Strands used in this project:

- **Agent Orchestration**: Coordinates tool selection and execution
- **Tool Integration**: Seamless integration with FastMCP servers
- **Multi-tool Management**: Handles multiple MCP tools in parallel
- **Context Management**: Maintains conversation state across interactions
- **Model-agnostic Design**: Works with various LLMs including AWS Bedrock models

The application uses the following Strands components:
```python
from strands import Agent
from strands.tools.mcp import MCPClient
from strands.models import BedrockModel
```

Strands Agents simplifies the process of building AI applications that can reason about user requests and use tools appropriately to fulfill those requests. In this project, it enables the LLM to:

1. Understand when to use math operations vs. weather queries
2. Call the appropriate FastMCP server tools
3. Format the responses back to the user through Chainlit

## License

[Specify your license]

## Acknowledgments

- Chainlit for the chat interface
- AWS Strands Agents for the powerful agent orchestration framework
- AWS Bedrock for model hosting and inference
- FastMCP for the MCP server implementation