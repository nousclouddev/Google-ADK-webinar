from google.adk.agents import Agent
from google.adk.tools import google_search

def get_weather(city: str) -> dict:
    """
    Returns the current weather for a given city (simulated data).
    """
    sample_data = {
        "kolkata": "30°C, humid and partly cloudy",
        "delhi": "28°C, dry and sunny",
        "mumbai": "32°C, warm with light rain",
        "bangalore": "25°C, pleasant and cloudy",
    }

    weather = sample_data.get(city.lower(), "Weather data not available")
    return {"city": city, "weather": weather}

root_agent = Agent(
    name="weather_tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent that provides weather information",
    instruction="""
    You are a helpful assistant that can use the following tool:
    - get_weather
    """,
    tools=[get_weather],
    # tools=[google_search],
    
)
