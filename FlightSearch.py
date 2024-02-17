import os
import requests
from dotenv import load_dotenv
from pprint import pprint
from datetime import datetime

class FlightSearch:

    def getIataCode(city):
        KIWI_API = os.environ['KIWI_API']

        # Example - https://api.tequila.kiwi.com/locations/query?term=Tel%20aviv&locale=en-US&location_types=airport&limit=1&active_only=true

        kiwi_endpoint = "https://api.tequila.kiwi.com/locations/query"

        kiwi_parameters = { "term": city, "locale": "en-US", "location_types": "airport", "limit": 1, "active_only": True}

        kiwi_headers = { "apikey" : KIWI_API }

        response = requests.get(url=kiwi_endpoint, params=kiwi_parameters, headers=kiwi_headers)

        return response.json()["locations"][0]["city"]["code"]





