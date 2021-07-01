from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_CODE = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

for data in sheet_data:
    if data["iataCode"] == "":
        city_names = [row["city"] for row in sheet_data]
        print(city_names)
        codes = flight_search.get_destination_code(city_names)
        data_manager.update_destination_codes(codes)
        sheet_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_CODE,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    try:
        price = flight.price
    except AttributeError:
        print(f"No flights found for {destination_code['iataCode']}")
    else:
        if flight is not None and flight.price < destinations[destination_code]["price"]:

            users = data_manager.get_customer_emails()
            emails = [row["email"] for row in users]
            names = [row["firstName"] for row in users]

            message = f"Low Price Alert! Only £{flight.price} to fly " \
                      f"from {flight.origin_city}->{flight.origin_airport} to " \
                      f"{flight.destination_city}->{flight.destination_airport}, from {flight.out_date} to " \
                      f"{flight.return_date}.\nAirline Name --> {flight.airline_name} " \
                      f"& \nOperating Carrier --> {flight.operating_carrier}"

            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

            link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}." \
                   f"{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

            notification_manager.send_sms(message)
            notification_manager.send_emails(emails=emails, message=message, google_flight_link=link)
