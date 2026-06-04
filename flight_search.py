import os
from dotenv import load_dotenv
import requests

load_dotenv()
SERAPI_ENDPOINT = "https://serpapi.com/search"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.serp_api_key = os.environ["SERP_API_KEY"]


    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        parameters = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time,
            "return_date": to_time,
            "type": "1",
            "adults": "1",
            "currency": "USD",
            "api_key": self.serp_api_key,
        }

        response = requests.get(SERAPI_ENDPOINT, params=parameters)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        flight_search_data = response.json()
        if "error" in flight_search_data:
            print(f"API error {flight_search_data['error']}")
            return None

        return flight_search_data