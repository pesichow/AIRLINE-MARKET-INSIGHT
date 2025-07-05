import pandas as pd
import streamlit as st

def process_flight_data(df):
    # Show column names in the app
    st.write("📌 Available columns in data:", df.columns.tolist())

    # Check for correct columns
    if not all(col in df.columns for col in ["from", "to"]):
        st.error("❌ Required columns 'from' and 'to' are missing in the dataset.")
        return pd.DataFrame()

    # Create route string
    df["route"] = df["from"] + " → " + df["to"]

    # Count and sort routes
    route_counts = df["route"].value_counts().reset_index()
    route_counts.columns = ["route", "count"]

    return route_counts.head(10)
