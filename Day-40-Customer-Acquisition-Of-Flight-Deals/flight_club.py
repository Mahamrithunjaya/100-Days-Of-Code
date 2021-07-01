import os
import time

import requests

print("Welcome to Subhajit's Flight Club.")
print("We find the best flight deals and email you.")

first_name = input("What is your first name?\n").title()
last_name = input("What is your last name?\n").title()

email_id = input("What is your email?\n")
email_id_check = input("Type your email again.\n")

while email_id != email_id_check:
    print("That's not right, two email-id's are different. Let's try again:")
    email_id = input("What is your email?\n")
    email_id_check = input("Type your email again.\n")

if email_id == email_id_check:
    print("Welcome.. Please Wait for your Registration.\n\n")
    time.sleep(4)

user_data = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email_id,
    }
}

response = requests.post(
    url=os.environ.get("SHEET_ENDPOINT"),
    json=user_data
)

if response.status_code == 200:
    print("Success! Your email has been added, look forwards to some amazing flight deals!")
else:
    print("There was an issue, please try again later.")
