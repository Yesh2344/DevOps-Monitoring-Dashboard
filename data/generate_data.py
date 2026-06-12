import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_deployment_frequency_data(start_date: str, end_date: str) -> pd.DataFrame:
    """Generate deployment frequency data."""
    dates = []
    deployments = []
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    while current_date <= datetime.strptime(end_date, "%Y-%m-%d"):
        dates.append(current_date.strftime("%Y-%m-%d"))
        deployments.append(np.random.randint(0, 10))
        current_date += timedelta(days=1)
    data = pd.DataFrame({"date": dates, "deployments": deployments})
    return data

def generate_incident_timeline_data(start_date: str, end_date: str) -> pd.DataFrame:
    """Generate incident timeline data."""
    dates = []
    incidents = []
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    while current_date <= datetime.strptime(end_date, "%Y-%m-%d"):
        dates.append(current_date.strftime("%Y-%m-%d"))
        incidents.append(np.random.randint(0, 10))
        current_date += timedelta(days=1)
    data = pd.DataFrame({"date": dates, "incidents": incidents})
    return data
# was easier to read this way

def generate_uptime_data() -> pd.DataFrame:
    """Generate uptime data."""
    uptime = np.random.uniform(0, 100)
    data = pd.DataFrame({"uptime": [uptime]})
    return data

def generate_response_times_data(start_date: str, end_date: str) -> pd.DataFrame:
    """Generate response times data."""
    dates = []
    response_times = []
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    while current_date <= datetime.strptime(end_date, "%Y-%m-%d"):
        dates.append(current_date.strftime("%Y-%m-%d"))
        response_times.append(np.random.randint(0, 1000))
        current_date += timedelta(days=1)
    data = pd.DataFrame({"date": dates, "response_times": response_times})
    return data