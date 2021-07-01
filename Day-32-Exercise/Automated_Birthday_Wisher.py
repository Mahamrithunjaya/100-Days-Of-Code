import pandas
import datetime as dt
import smtplib
import random
import os

PLACEHOLDER = "[NAME]"
MY_EMAIL = "**********@gmail.com"
MY_PASSWORD = "**********"
SENDER_NAME = "********"

# ********** CSV DATA HANDLING ********** #

data = pandas.read_csv("birthdays.csv")
birthday_dict = data.to_dict(orient="records")
# birthday_dict = {(data_row.month, data_row.day): data_row for(index, data_row) in data.iterrows()}

# ********** PRESENT DATE CHECKING ********** #

now = dt.datetime.now()
today_day = now.date().strftime("%d")
today_month = now.date().strftime("%m")
today_tuple = (int(today_month), int(today_day))

# ********** BIRTHDAY DATE CHECKING ********** #

for birthday in birthday_dict:
    month_day_birth = (birthday["month"], birthday["day"])

    # ********** LETTER CHOICE PICKER & LETTER HANDLING & SENDING ********** #
    if today_tuple == month_day_birth:
        birthday_name = birthday["name"]
        birthday_email = birthday["email"]
        filename = random.choice(os.listdir('letter_templates'))
        # file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file=f"letter_templates/{filename}", mode="r") as letter_file:
            letter_contents = letter_file.read()

        birthday_letter = letter_contents.replace(PLACEHOLDER, birthday_name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # Securing the connection
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_email,
                msg=f"From: \"{SENDER_NAME}\"<{MY_EMAIL}>\n"
                    f"To: {birthday_email}\n"
                    f"Subject: Happy Birthday!!\n\n{birthday_letter}"
            )
