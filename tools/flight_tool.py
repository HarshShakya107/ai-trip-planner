import json
from langchain.tools import tool

@tool
def search_flight(source: str, destination: str) -> dict:
    """
    Finds the cheapest flight from source to destination.
    """
    if "to" in source.lower() or "to" in destination.lower():
        return {"error": "Provide only city names, not 'City1 to City2'."}
    
    with open("flights.json") as f:
        flights = json.load(f)
    
    options = [f for f in flights if f['from'].lower() == source.lower() and f['to'].lower() == destination.lower()]
    
    if not options:
        return {"error": "No flights found."}
    
    cheapest = min(options, key=lambda x: x['price'])
    return cheapest




