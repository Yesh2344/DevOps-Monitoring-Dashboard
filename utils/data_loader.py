import pandas as pd
from typing import List, Dict

def load_data(file_path: str) -> pd.DataFrame:
    """Load data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """Process data by handling missing values and converting data types."""
    try:
        data.fillna(0, inplace=True)
        data["date"] = pd.to_datetime(data["date"])
        return data
    except Exception as e:
        print(f"Error processing data: {e}")
        return None

def get_deployment_frequency(data: pd.DataFrame) -> pd.DataFrame:
    """Get deployment frequency data."""
    try:
        deployment_frequency = data.groupby("date")["deployments"].sum().reset_index()
        return deployment_frequency
    except Exception as e:
        print(f"Error getting deployment frequency: {e}")
        return None

def get_incident_timeline(data: pd.DataFrame) -> pd.DataFrame:
    """Get incident timeline data."""
    try:
        incident_timeline = data.groupby("date")["incidents"].sum().reset_index()
        return incident_timeline
    except Exception as e:
        print(f"Error getting incident timeline: {e}")
        return None

def get_uptime(data: pd.DataFrame) -> pd.DataFrame:
    """Get uptime data."""
    try:
        uptime = data["uptime"].mean().reset_index()
        return uptime
    except Exception as e:
        print(f"Error getting uptime: {e}")
        return None

def get_response_times(data: pd.DataFrame) -> pd.DataFrame:
    """Get response times data."""
    try:
        response_times = data.groupby("date")["response_times"].mean().reset_index()
        return response_times
    except Exception as e:
        print(f"Error getting response times: {e}")
        return None