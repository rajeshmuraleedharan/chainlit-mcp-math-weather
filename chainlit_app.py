import chainlit as cl
from strands import Agent
from strands.tools.mcp import MCPClient
from strands.models import BedrockModel, ollama
from mcp import stdio_client, StdioServerParameters

import ssl
import certifi
ssl_context = ssl.create_default_context(cafile=certifi.where())

# MCP tools launched via stdio subprocesses
math_tool = MCPClient(lambda: stdio_client(StdioServerParameters(command="python", args=["mcp_servers/math_mcp_server.py"]))) # type: ignore
weather_tool = MCPClient(lambda: stdio_client(StdioServerParameters(command="python", args=["mcp_servers/weather_mcp_server.py"]))) # type: ignore
#llm = ollama(model="llama3.1", # type: ignore
              #temperature=0.2,)

llm = BedrockModel(
    model="us.meta.llama3-1-8b-instruct-v1:0", #type: ignore
    temperature=0.2,
    region_name="us-east-1" # type: ignore
) # type: ignore

SYSTEM_PROMPT = """
You are a helpful multi-tool agent that can perform math calculations and fetch weather information.

You have access to the following tools:
1. Math Tool: Perform mathematical calculations.
2. Weather Tool: Fetch weather information.

When the user asks a math question, call the Math Tool with the expression as input.

When the user asks about weather, call the Weather Tool with JSON input exactly in this format:
{"city": "<city_name>"}

Example:
User: What's the weather in Austin?
Assistant: get_weather({"city": "Austin"})
User: The weather in Austin is Sunny, 90°F.

Only use the tools when necessary. Return only the tool output as your answer.
"""

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content=(
            "👋 Hi! I'm your multi-tool agent.\n\n"
            "You can ask:\n"
            "- 🧮 Math: `What is 12 * (3 + 4)`\n"
            "- 🌤️ Weather: `What's the weather in Austin?`"
        )
    ).send()

@cl.on_message
async def on_message(message: cl.Message):
    user_text = message.content # type: ignore
    
  
    # Launch both MCP tools via stdio
    with math_tool, weather_tool:
        tools = math_tool.list_tools_sync() + weather_tool.list_tools_sync()
        agent = Agent(model=llm, 
                      tools=tools,
                      system_prompt=SYSTEM_PROMPT)

        response = agent(user_text)

    await cl.Message(content=response).send() # type: ignore