import os


from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search

from travel_planner_agent.instructions import (
    ITINERARY_PLANNER_AGENT_INSTRUCTIONS,
    BUDGET_AGENT_INSTRUCTIONS,
    DEMO_ORCHESTRATOR_INSTRUCTION
)

itinerary_planner_agent = LlmAgent(
    name="ItineraryPlanner",
    model="gemini-2.0-flash",
    description="An agent that creates a detailed, personalized travel itinerary based on user input.",
    instruction=ITINERARY_PLANNER_AGENT_INSTRUCTIONS,
    tools=[google_search],
    output_key="itinerary_summary"  # Save result to state under this key
)

budget_agent = LlmAgent(
    name="BudgetAgent",
    model="gemini-2.0-flash",  
    description="An agent that creates a detailed financial budget for a trip based on the itinerary provided by the Itinerary Planner Agent.", 
    instruction=BUDGET_AGENT_INSTRUCTIONS,
    tools=[google_search],  # This agent can also use the Google Search tool
    # This agent will automatically receive the output of the previous agent 
    output_key="budget_summary"  # Save result to state under this key
)



Demo_orchestrator = SequentialAgent(
    name="TravelPlannerAgent",
    description=DEMO_ORCHESTRATOR_INSTRUCTION,
    sub_agents=[
        itinerary_planner_agent,
        budget_agent,
    ]
)

root_agent = Demo_orchestrator