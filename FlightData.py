import os
import requests
from dotenv import load_dotenv
from pprint import pprint
from datetime import datetime
import FlightSearch

class FlightData:
    # Example = https://api.tequila.kiwi.com/v2/search?fly_from=TLV&fly_to=PAR&date_from=01%2F03%2F2024&date_to=01%2F08%2F2024
# &nights_in_dst_from=3&nights_in_dst_to=7&max_fly_duration=20&one_for_city=1&one_per_date=0&selected_cabins=M&adult_hold_bag=0&adult_hand_bag=1
# &partner_market=us&curr=USD&locale=en&max_stopovers=2&max_sector_stopovers=2

    def getFlightData(fly_to):
        KIWI_API = os.environ['KIWI_API']

        kiwi_endpoint = "https://api.tequila.kiwi.com/v2/search"

        kiwi_parameters = { "fly_from": "TLV", "fly_to": fly_to, "date_from": "01/03/2024", "date_to": "01/08/2024", "nights_in_dst_from": 3, "nights_in_dst_to": 7, "max_fly_duration": 20, "one_for_city": 1, "one_per_date": 0, "selected_cabins": "M", "adult_hold_bag": 0, "adult_hand_bag": 1, "partner_market": "us", "curr": "USD", "locale": "en", "max_stopovers": 2, "max_sector_stopovers": 2}

        kiwi_headers = { "apikey" : KIWI_API }

        response = requests.get(url=kiwi_endpoint, params=kiwi_parameters, headers=kiwi_headers)

        data = response.json()
        #print(data)

        price = data["data"][0]["price"]
        flyto = data["data"][0]["flyTo"]
        if len(data["data"][0]["route"]) > 2:
            citystop = data["data"][0]["route"][0]["cityTo"]
        else:
            citystop = "DIRECT"
        return price, flyto, citystop





