from pprint import pprint
import requests
import os
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ.get("TQ_API_KEY")


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "term": city_name,
            "location_types": "city",
        }
        response = requests.get(
            url=location_endpoint,
            headers=headers,
            params=query
        )
        response.raise_for_status()
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 20,
            "flight_type": "round",
            "vehicle_type": "aircraft",
            "max_stopovers": 0,
            "curr": "GBP",
        }
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print("Exception activated!")
            query["max_stopovers"] = 2
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            try:
                data = response.json()["data"][0]
                # pprint(data)
            except IndexError:
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0],
                    stop_overs=2,
                    via_city=data["route"][0]["cityTo"],
                    airline_name=data["route"][0]["airline"],
                    operating_carrier=data["route"][0]["operating_carrier"]
                )
                print(f"{flight_data.destination_city}: £{flight_data.price} "
                      f"--> Airline: {flight_data.airline_name} --> Operating Carrier: {flight_data.operating_carrier}")
                return flight_data

        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                airline_name=data["route"][0]["airline"],
                operating_carrier=data["route"][0]["operating_carrier"]
            )
            print(f"{flight_data.destination_city}: £{flight_data.price} "
                  f"--> Airline: {flight_data.airline_name} --> Operating Carrier: {flight_data.operating_carrier}")
            return flight_data
