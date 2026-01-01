from langchain.tools import tool

@tool
def estimate_budget(flight_price: int, hotel_price_per_night: int, days: int, extra: int = 2000) -> dict:
    """
    Calculates total trip cost.
    extra: estimated food & travel per trip
    """
    hotel_total = hotel_price_per_night * days
    total = flight_price + hotel_total + extra
    return {
        "flight": flight_price,
        "hotel": hotel_total,
        "food_travel": extra,
        "total": total
    }

