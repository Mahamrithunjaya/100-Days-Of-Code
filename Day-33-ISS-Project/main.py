import requests
import datetime as dt
import time
import smtplib
from dateutil.parser import isoparse

MY_LONG = 88.543700
MY_LAT = 26.542340
MY_EMAIL = "*******@gmail.com"
MY_PASSWORD = "******"
RECIPIENT_EMAIL = "********@yahoo.com"
SENDER_NAME = "*******"


def date_time_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = dt.datetime.fromtimestamp(now_timestamp) - dt.datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Our position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    # sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise = isoparse(data["results"]["sunrise"])
    sunset = isoparse(data["results"]["sunset"])

    # Convert from UTC to Local
    sunrise = date_time_from_utc_to_local(sunrise).strftime("%H:%M:%S")
    sunset = date_time_from_utc_to_local(sunset).strftime("%H:%M:%S")

    time_now = dt.datetime.now().strftime("%H:%M:%S")
    print(time_now)
    if time_now >= sunset or time_now <= sunrise:
        return True


run_time = 0
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # Securing the connection
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECIPIENT_EMAIL,
                msg=f"From: \"{SENDER_NAME}\"<{MY_EMAIL}>\n"
                    f"To: {RECIPIENT_EMAIL}\n"
                    "Subject:Look up\n\nThe ISS is above you in the sky."
            )
    run_time += 1
    print(f"Running {run_time}")
