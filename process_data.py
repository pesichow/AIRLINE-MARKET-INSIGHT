import pandas as pd
import streamlit as st

def process_flight_data(df):
    # Show available columns for debugging
    st.write("📌 Available columns in data:", df.columns.tolist())

    # Check for required columns
    if not all(col in df.columns for col in ["origin", "destination"]):
        st.error("❌ Required columns 'origin' and 'destination' are missing in the dataset.")
        return pd.DataFrame()

    # Create a combined route string
    df["route"] = df["origin"] + " → " + df["destination"]

    # Count the number of times each route appears
    route_counts = df["route"].value_counts().reset_index()
    route_counts.columns = ["route", "count"]

    # Return the top 10 most popular routes
    return route_counts.head(10)
