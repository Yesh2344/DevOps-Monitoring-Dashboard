import streamlit as st
from utils.charts import create_deployment_frequency_chart, create_incident_timeline_chart, create_uptime_gauge_chart, create_response_times_chart
from utils.data_loader import load_data, process_data, get_deployment_frequency, get_incident_timeline, get_uptime, get_response_times
from config import DashboardConfig
import pandas as pd

def main():
    """Main function."""
    config = DashboardConfig()
    st.title(config.title)
    st.sidebar.title(config.title)
    pages = ["Deployment Frequency", "Incident Timeline", "Uptime", "Response Times"]
    page = st.sidebar.selectbox("Select Page", pages)

    if page == "Deployment Frequency":
        data = load_data("data/deployment_frequency.csv")
        data = process_data(data)
        deployment_frequency = get_deployment_frequency(data)
        chart = create_deployment_frequency_chart(deployment_frequency)
        st.plotly_chart(chart, use_container_width=True)

    elif page == "Incident Timeline":
        data = load_data("data/incident_timeline.csv")
        data = process_data(data)
        incident_timeline = get_incident_timeline(data)
        chart = create_incident_timeline_chart(incident_timeline)
        st.plotly_chart(chart, use_container_width=True)

    elif page == "Uptime":
        data = load_data("data/uptime.csv")
        data = process_data(data)
        uptime = get_uptime(data)
        chart = create_uptime_gauge_chart(uptime)
        st.plotly_chart(chart, use_container_width=True)

    elif page == "Response Times":
        data = load_data("data/response_times.csv")
        data = process_data(data)
        response_times = get_response_times(data)
        chart = create_response_times_chart(response_times)
        st.pyplot(chart)

if __name__ == "__main__":
    main()