import streamlit as st
import pandas as pd
import plotly.express as px
from fetch_data import fetch_flight_data
from process_data import process_flight_data
from summary_ai import generate_summary

# Set up Streamlit page
st.set_page_config(page_title="✈️ Airline Market Demand", layout="wide")
st.title("📊 Airline Market Demand Insights")

# Button to fetch and display data
if st.button("Fetch Latest Data"):
    with st.spinner("Fetching and processing data..."):
        # Step 1: Fetch data from API
        data = fetch_flight_data()
        
        if data is None or data.empty:
            st.error("❌ Could not fetch data or data is empty.")
        else:
            # Step 2: Process data
            top_routes_df = process_flight_data(data)

            # Step 3: Show chart
            st.subheader("✈️ Top 10 Popular Flight Routes")
            fig = px.bar(
                top_routes_df,
                x="route",
                y="count",
                labels={"route": "Route", "count": "Number of Flights"},
                title="Top 10 Most Frequent Flight Routes",
                color="count",
                color_continuous_scale="Blues"
            )
            st.plotly_chart(fig, use_container_width=True)

            # Step 4: AI Summary
            st.subheader("🧠 AI-Generated Summary")
            combined_text = " ".join(top_routes_df["route"] + " appeared " + top_routes_df["count"].astype(str) + " times.")
            summary = generate_summary(combined_text)
            st.success(summary)

# Optional info
st.markdown("---")
st.markdown("Developed by Pallapothu Prasad | Powered by Streamlit & Hugging Face Transformers")
