import requests
from twilio.rest import Client

api_key = "350c6e1a2bb58cb46e20636f2a3f21c9"
account_sid = "YOUR_SID"
auth_token = "YOUR_TOKEN"

weather_parameters = {
    "lat": 25.152839,
    "lon": 92.4000228,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall", params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

hourly_list = weather_data["hourly"][:12]
# print(weather_data["hourly"][0]["weather"][0]["id"])

will_rain = False

for hour_data in hourly_list:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain🌧️⛈️. Bring an Umbrella ☔.",
        from_='YOUR_TRIAL_NUMBER',
        to='YOUR_SENDING_NUMBER'
    )
    print(message.status)
