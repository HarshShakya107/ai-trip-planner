import os
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from tools.flight_tool import search_flight
from tools.hotel_tool import recommend_hotel
from tools.places_tool import discover_places
from tools.weather_tool import get_weather
from tools.budget_tool import estimate_budget

tools = [
    search_flight,
    recommend_hotel,
    discover_places,
    get_weather,
    estimate_budget
]

llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS, 
    verbose=True
)


