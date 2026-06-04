import requests_cache
from pprint import pprint
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

#Conserves requests
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*" : requests_cache.DO_NOT_CACHE,
        "*" : 3600,
    }
)

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

#Talks to Sheety
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)

#Sets the dates
today = datetime.now()
tomorrow = today + timedelta(days=1)
tomorrow = tomorrow.strftime("%Y-%m-%d")
six_months_from_today = today + timedelta(days= (6 * 30))
six_months_from_today = six_months_from_today.strftime("%Y-%m-%d")

#Does a Flight Search

ORIGIN_CITY_IATA = "IAH"

for destination in sheet_data:
    pprint(f"Getting flights for {destination['city']}...")
    flight_search_data = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time = tomorrow,
        to_time = six_months_from_today,
    )

    #Shows the Cheapest Flight
    cheapest_flight = find_cheapest_flight(flight_search_data, return_date=six_months_from_today)
    pprint(f"{destination['city']}: USD {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        pprint(f"Lower price flight found to {destination['city']}!")
        data_manager.update_lowest_price(destination['id'], cheapest_flight.price)
        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only USD {cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )