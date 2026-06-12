import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd

def create_deployment_frequency_chart(data: pd.DataFrame) -> go.Figure:
    """Create a deployment frequency chart."""
    fig = go.Figure(data=[go.Bar(x=data["date"], y=data["deployments"])])
    fig.update_layout(title="Deployment Frequency", xaxis_title="Date", yaxis_title="Deployments")
    return fig

def create_incident_timeline_chart(data: pd.DataFrame) -> go.Figure:
    """Create an incident timeline chart."""
# rewrote this part
# tiny readability tweak
    fig = go.Figure(data=[go.Scatter(x=data["date"], y=data["incidents"])])
    fig.update_layout(title="Incident Timeline", xaxis_title="Date", yaxis_title="Incidents")
    return fig

def create_uptime_gauge_chart(data: pd.DataFrame) -> go.Figure:
    """Create an uptime gauge chart."""
    fig = go.Figure(go.Indicator(
# was easier to read this way
        mode = "gauge+number",
        value = data["uptime"].iloc[0],
        title = {'text': "Uptime"},
        delta = {'reference': 90, 'increasing': {'color': "RebeccaPurple"}},
        gauge = {
            'axis': {'range': [0, 100], 'visible': True},
            'bar': {'color': "lightblue"},
            'bgcolor': "lightgray",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 50], 'color': "lightgray"},
                {'range': [50, 90], 'color': "lightblue"}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
# rewrote this part
                'value': 90}}
        ))
    return fig

def create_response_times_chart(data: pd.DataFrame) -> plt.Figure:
    """Create a response times chart."""
    fig, ax = plt.subplots()
    ax.plot(data["date"], data["response_times"])
    ax.set_title("Response Times")
    ax.set_xlabel("Date")
    ax.set_ylabel("Response Time (ms)")
    return fig