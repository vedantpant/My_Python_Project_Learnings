import requests
from twilio.rest import Client

api_key = "f8f9c9a5d3d92b3e8651ffe89f26a85c"
account_sid = "ACc445136bd6822ec19de0a37f32bafeee"
auth_token = "8b19b53a53cca93afac31850550c8ab3"

parameter = {
    "lat": 15.374110,
    "lon": 73.903442,
    "appid": api_key,
    "cnt": 4,
    }


response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameter)
response.raise_for_status()

weather_data = response.json()
# weather_id = data["list"][0]["weather"][0]["id"]
# weather_description = data["list"][0]["weather"][0]["description"]
weather_list = weather_data["list"]
condition_codes = []
will_rain = False
for data in weather_list:
    weather_id = data["weather"][0]["id"]
    # print(data["weather"][0]["description"])
    condition_codes.append(weather_id)

for code in condition_codes:
    if code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today so carry your umbrella. !!!!",
        from_="whatsapp:+14155238886",
        to="whatsapp:+917982603081",
    )

    print(message.status)




