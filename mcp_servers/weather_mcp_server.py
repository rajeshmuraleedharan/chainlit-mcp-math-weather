from fastmcp import FastMCP
from pydantic import BaseModel

mcp = FastMCP("My simple weather MCP server")

class WeatherInput(BaseModel):
    city: str

@mcp.tool
async def get_weather(input: str):
    """
    Get the weather forecast for a city.
    Input: city (str) - The name of the city to get the weather for.
    Output: A dictionary with the weather forecast.
    Example:
    get_weather({"city": "Austin"})
    """
    # Simulating a weather API call with a static response
    fake_weather = {
        "austin": "Sunny, 90°F",
        "new york": "Rainy, 70°F"
    }
    city = input.lower()
    return {"forecast": fake_weather.get(city, "No data available")}

if __name__ == "__main__":
    mcp.run()