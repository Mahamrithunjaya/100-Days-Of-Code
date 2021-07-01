import requests
import os
from twilio.rest import Client

api_key = os.environ.get("WEATHER_API_KEY")
account_sid = os.environ.get("SID_KEY")
auth_token = os.environ.get("AUTH_TOKEN")

weather_parameters = {
    "lat": os.environ.get("LATITUDE"),
    "lon": os.environ.get("LONGITUDE"),
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall", params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

hourly_list = weather_data["hourly"][:12]
# print(weather_data["hourly"][0]["weather"][0]["id"])

will_rain = False
message = ""
for hour_data in hourly_list:
    condition_code = hour_data["weather"][0]["id"]
    if 200 <= int(condition_code) <= 232:
        message = "Warning ⚠️Today there might be THUNDERSTORM ⛈️🌩️."
        will_rain = True
    elif 300 <= int(condition_code) <= 321:
        message = "It's going to DRIZZLE 🌧️.\n Bring an Umbrella ☔ ."
        will_rain = True
    elif 500 <= int(condition_code) <= 531:
        message = "Warning ⚠ It's going to rain ⛆ 🌦️ ⛈️\nBring an Umbrella ☔."
        will_rain = True
    elif 600 <= int(condition_code) <= 622:
        message = "It's going to snow 🌨️  \nYou may take an Umbrella☂️."
        will_rain = True
    elif 701 <= int(condition_code) <= 781:
        message = "Warning ⚠️It's going to Atmosphere (Mist or Smoke or Haze or Dust or Fog or Sand)️."
        will_rain = True
    elif int(condition_code) == 800:
        message = "It's clear outside ⛱️."
        will_rain = True
    elif 801 <= int(condition_code) <= 804:
        message = "It's cloudy day ☁️⛅  🌤️ ️."
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=os.environ.get("FROM_NUMBER"),
        to=os.environ.get("TO_NUMBER")
    )
    print(message.status)
