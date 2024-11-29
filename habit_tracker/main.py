import requests
from datetime import datetime

USERNAME = "vedantisamazing"
TOKEN = "uih5i6yul45f5458lufg56gi"
GRAPH_ID = "graph1"
DATE = "20240706"
QUANTITY = "1"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "coding_graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime(year=2023, month=7, day=6)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": QUANTITY,
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

put_endpoint = f"{pixel_endpoint}/{today.strftime("%Y%m%d")}"

put_config = {
    "quantity": "0.5",
}

response = requests.delete(url=put_endpoint, headers=headers)
print(response.text)
