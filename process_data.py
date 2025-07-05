import pandas as pd

def process_flight_data(df):
    # If df is already a DataFrame, don't read from file
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")

    # Combine departure & arrival into a single route string
    df["route"] = df["departure_airport"] + " → " + df["arrival_airport"]

    # Count route frequencies
    top_routes = df["route"].value_counts().reset_index()
    top_routes.columns = ["route", "count"]

    # Return top 10
    return top_routes.head(10)
