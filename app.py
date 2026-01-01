
import streamlit as st
from agent import agent_executor

st.set_page_config("AI Trip Planner", layout="wide")
st.title("🧭 AI Trip Planner")

from_city = st.text_input("Departure City")
to_city = st.text_input("Arrival City")
days = st.number_input("Number of Days", min_value=1, max_value=7, value=3)
budget = st.number_input("Budget (₹)", min_value=20000, step=500)

if st.button("Generate Trip Itinerary"):
    if not from_city or not to_city:
        st.error("Please enter both departure and arrival cities.")
    else:
        
        query_str = (
            f"Plan a trip from {from_city} to {to_city} "
            f"for {days} days with a budget of ₹{budget}. "
            "Include travel, accommodation, food, and sightseeing recommendations."
        )

        with st.spinner("Planning your trip..."):
           
            try:
                result = agent_executor.run(query_str)
                
                
                st.subheader("Trip Summary")
                st.markdown(result) 

            except Exception as e:
                st.error(f"Error generating trip: {e}")





 

