import requests
import datetime as dt
import time
import smtplib
from pytz import timezone

MY_LONG = 88.543700
MY_LAT = 26.542340
MY_EMAIL = "*****@gmail.com"
MY_PASSWORD = "******"
RECIPIENT_EMAIL = "******@yahoo.com"
SENDER_NAME = "*****"


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

    # Accessing "sunrise" and "sunset" data from JSON and Converting that from UTC to Local
    sunrise = dt.datetime.strptime(data["results"]["sunrise"],
                                   '%Y-%m-%dT%H:%M:%S%z').astimezone(timezone('Asia/Kolkata'))
    sunset = dt.datetime.strptime(data["results"]["sunset"],
                                  '%Y-%m-%dT%H:%M:%S%z').astimezone(timezone('Asia/Kolkata'))

    # Taking out only the time in the format of HOUR:MINUTE:SECOND
    sunrise = sunrise.strftime("%H:%M:%S")
    sunset = sunset.strftime("%H:%M:%S")

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
