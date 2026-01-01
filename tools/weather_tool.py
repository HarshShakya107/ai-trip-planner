import requests
from langchain.tools import tool

@tool
def get_weather(lat: float, lon: float, days: int) -> dict:
    """
    Calls Open-Meteo API and returns weather for the next 'days' days.
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,weathercode&timezone=auto"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "Failed to fetch weather."}
    
    data = response.json()
    daily_temp = data['daily']['temperature_2m_max'][:days]
    weather_list = []
    
    for i, temp in enumerate(daily_temp, 1):
        weather_list.append({"day": i, "forecast": f"{temp}°C"})
    
    return weather_list


