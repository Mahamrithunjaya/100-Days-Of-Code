import os
import requests
from datetime import datetime

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT_URL")

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 164.592
AGE = 21

exercise_text = input("Tell me which exercise you did: ")

nutrition_headers = {
    "x-app-id": os.environ.get("NUTRITION_APP_ID"),
    "x-app-key": os.environ.get("NUTRITION_API_KEY"),
    "x-remote-user-id": "0",
}

request_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

bearer_headers = {
    "Authorization": f"Bearer {os.environ.get('TOKEN')}"
}

exercise_response = requests.post(url=EXERCISE_ENDPOINT, headers=nutrition_headers, json=request_parameters)
exercise_response.raise_for_status()
data = exercise_response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%I:%M:%S %p")

for exercise in data["exercises"]:
    sheet_parameters = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": f"{exercise['duration_min']}min",
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_parameters, headers=bearer_headers)
    print(sheety_response.text)
