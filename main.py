import json
import os
import requests
from dotenv import load_dotenv
from pprint import pprint
from datetime import datetime
from FlightSearch import FlightSearch
from FlightData import FlightData

# .env file contains api keys in the format of API_KEY="xxxxxx", get it using os.environ['API_KEY']
load_dotenv()  # take environment variables from .env.



Date = datetime.now().strftime("%d/%m/%Y")
Time = datetime.now().strftime("%H:%M:%S")

sheety_endpoint = "https://api.sheety.co/27e3609a0241b7d56179d12188a416ea/flightDeals/prices"

# sheety_parmaters = { "workout": { "Date": Date, "Time": Time, "Exercise": Exercise, "Duration": Duration,"Calories": Calories} }
# sheety_headers = { "Authorization" : "Bearer Dana5212" }


response2 = requests.get(url=sheety_endpoint)
sheet_data = response2.json()["prices"]
pprint(sheet_data)
for row in sheet_data:
    row["iataCode"] = FlightSearch.getIataCode(row["city"])



# update sheet row table with new data using put request
# for row in sheet_data:
#     city = row["city"]
#     iataCode = row["iataCode"]
#     lowestPrice = row["lowestPrice"]
#     id = row["id"]
#
#     row_parmas = {
#         "price": {
#             "city": city,
#             "iataCode": iataCode,
#             "lowestPrice": lowestPrice,
#             "id": id,
#         }
#     }
#     put_api = sheety_endpoint+"/" + str(id)
#     response = requests.put(url=put_api, json=row_parmas)
#
# response2 = requests.get(url=sheety_endpoint)
# sheet_data = response2.json()["prices"]
# pprint(sheet_data)
for row in sheet_data:
    new_price, flyto , cityto = FlightData.getFlightData(row["iataCode"])
    print (new_price)
    if int(new_price) < int(row["lowestPrice"]):
        if cityto != "DIRECT":
            print (f"found new Lowest price for flight from Tel-Aviv(TLV) to {row['city']}({flyto}) is ${str(new_price)}; old price was ${str(row['lowestPrice'])}\nFlight has 1 stoppover in {cityto}")
        else:
            print (f"found new Lowest price for flight from Tel-Aviv(TLV) to {row['city']}({flyto}) is ${str(new_price)}; old price was ${str(row['lowestPrice'])}\nFlight has no stops")
    else:
        print ("Could NOT found new Lowest price for flight from Tel-Aviv to " + row["city"] + "; old data is $" + str(row["lowestPrice"]))


# Users code is on Replit at https://replit.com/@yuvalco1/Yuvals-flight-club
