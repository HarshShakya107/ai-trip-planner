import json
from langchain.tools import tool

@tool
def recommend_hotel(city: str, budget: int) -> dict:
    """
    Pick the highest-rated hotel within the given budget in the specified city.
    Returns hotel details: name, stars, price_per_night, and city.
    """
    with open("hotels.json") as f:
        hotels = json.load(f)
    
    options = [h for h in hotels if h['city'].lower() == city.lower() and h['price_per_night'] <= budget]
    
    if not options:
        return {"error": "No hotels found in your budget."}
    
    best = max(options, key=lambda x: x['stars'])
    return best

