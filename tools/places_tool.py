import json
from langchain.tools import tool

@tool
def discover_places(city: str, days: int) -> dict:
    """
   Returns a day-wise itinerary of top-rated places to visit in the given city.
    Picks up to 2 places per day from places.json.
    """
    with open("places.json") as f:
        places = json.load(f)
    
    city_places = [p for p in places if p['city'].lower() == city.lower()]
    
    if not city_places:
        return {"error": "No places found."}
    
 
    city_places.sort(key=lambda x: x.get('rating', 0), reverse=True)
    
    
    itinerary = {}
    for day in range(1, days + 1):
        
        day_places = city_places[(day-1)*2 : day*2]
        itinerary[f"day_{day}"] = [p['name'] for p in day_places]
    
    return itinerary


