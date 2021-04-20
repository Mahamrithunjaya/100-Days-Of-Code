import requests
from twilio.rest import Client
import config_parameter

api_key = config_parameter.weather_api_key
account_sid = config_parameter.sid_key
auth_token = config_parameter.token_sms

weather_parameters = {
    "lat": config_parameter.latitude,
    "lon": config_parameter.longitude,
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
        from_=config_parameter.from_number,
        to=config_parameter.to_number
    )
    print(message.status)
