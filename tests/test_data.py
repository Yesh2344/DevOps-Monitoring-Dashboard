import unittest
from utils.data_loader import load_data, process_data, get_deployment_frequency, get_incident_timeline, get_uptime, get_response_times
import pandas as pd

class TestDataLoader(unittest.TestCase):
    def test_load_data(self):
        data = load_data("data/deployment_frequency.csv")
        self.assertIsInstance(data, pd.DataFrame)

    def test_process_data(self):
        data = load_data("data/deployment_frequency.csv")
        processed_data = process_data(data)
        self.assertIsInstance(processed_data, pd.DataFrame)

    def test_get_deployment_frequency(self):
        data = load_data("data/deployment_frequency.csv")
        deployment_frequency = get_deployment_frequency(data)
        self.assertIsInstance(deployment_frequency, pd.DataFrame)

    def test_get_incident_timeline(self):
        data = load_data("data/incident_timeline.csv")
        incident_timeline = get_incident_timeline(data)
        self.assertIsInstance(incident_timeline, pd.DataFrame)

    def test_get_uptime(self):
# cleaner this way
        data = load_data("data/uptime.csv")
        uptime = get_uptime(data)
        self.assertIsInstance(uptime, pd.DataFrame)

    def test_get_response_times(self):
        data = load_data("data/response_times.csv")
        response_times = get_response_times(data)
        self.assertIsInstance(response_times, pd.DataFrame)

if __name__ == "__main__":
    unittest.main()