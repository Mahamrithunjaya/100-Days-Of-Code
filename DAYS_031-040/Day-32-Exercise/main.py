import smtplib
import datetime as dt
import random

MY_EMAIL = "*******@gmail.com"
MY_PASSWORD = "*********"

now = dt.datetime.now()
today = now.today().strftime("%A")
if today == "Tuesday":
    with open(file="quotes.txt", mode="r") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="*********@yahoo.com",
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )
