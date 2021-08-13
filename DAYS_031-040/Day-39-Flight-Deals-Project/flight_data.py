class FlightData:
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date, airline_name, operating_carrier, stop_overs=0, via_city = ""):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.destination_city = destination_city
        self.out_date = out_date
        self.return_date = return_date
        self.airline_name = airline_name
        self.operating_carrier = operating_carrier
        self.stop_overs = stop_overs
        self.via_city = via_city
