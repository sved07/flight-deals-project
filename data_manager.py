import requests
import os
from dotenv import load_dotenv

SHEETY_URL = "https://api.sheety.co/a3e7508aa308dc15921cbad4bf5aefee/flightDeals/prices"
load_dotenv()


class DataManager:
    #This class is responsible for talking to the Google Sheet.



    def __init__(self):
        self.destination_data = {}
        self.sheety_token = os.getenv("SHEETY_TOKEN")

        self.headers = {
            "Authorization": f"Bearer {self.sheety_token}",
        }

    def get_destination_data(self):
        response = requests.get(SHEETY_URL, headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price" :{
                "lowestPrice": new_price,
            }
        }

        requests.put(
            url= f"{SHEETY_URL}/{row_id}",
            json= new_data,
            headers=self.headers
        )
