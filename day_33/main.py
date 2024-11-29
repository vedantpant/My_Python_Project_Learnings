import requests
from datetime import datetime

MY_LAT = 29.203951
MY_LNG = 78.959686
FORMAT = 0

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(data)
# iss_position = data["iss_position"]
# print(iss_position["latitude"])
# print(iss_position["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": FORMAT,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
