from google.adk.agents import Agent

root_agent = Agent(
    name="quote_agent",
    model="gemini-2.0-flash",
    description="Motivational quote generator agent",
    instruction="""
    You are an assistant that provides short motivational quotes.
    When a user interacts, share one inspiring quote each time.
    Keep the tone positive and encouraging.
    """,
)