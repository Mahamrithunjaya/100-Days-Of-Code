import requests
import os

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT_URL")


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):

        response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self, codes):

        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": codes
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = os.environ.get("SHEET_USER_ENDPOINT")
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]

        return self.customer_data
