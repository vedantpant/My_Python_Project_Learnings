import requests
from datetime import datetime
import os

APP_ID = os.environ["ENV_APP_ID"]
API_KEY = os.environ["ENV_API_KEY"]
SHEET_AUTH_KEY = os.environ["ENV_SHEET_AUTH_KEY"]

exercise_hyperlink = os.environ["ENV_exercise_hyperlink"]
exercise_endpoint = os.environ["ENV_exercise_endpoint"]

combined_endpoint = f"{exercise_hyperlink}{exercise_endpoint}"

query_input = input("enter the amount of exercise you did today?:")

exercise_param = {
    "query": query_input,
}

exercise_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=combined_endpoint, json=exercise_param, headers=exercise_header)

result = response.json()

sheet_hyperlink = os.environ["ENV_sheet_hyperlink"]

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_auth_header = {
    "Authorization": SHEET_AUTH_KEY,
}

sheet_response = requests.post(url=sheet_hyperlink, json=sheet_inputs, headers=sheet_auth_header)
print(sheet_response.text)





