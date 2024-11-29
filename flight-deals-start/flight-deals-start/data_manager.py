import requests
import time

class DataManager:
    def __init__(self):
        self.get_sheet_data = "https://api.sheety.co/a1802de5c826c72620fa0fab202b701f/flightDeals/prices"
        self.auth_header = {"Authorization": "Basic dmVkYW50MDgxMjpTaWdtYUAxMjM="}
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.get_sheet_data, headers=self.auth_header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def put_data_in_sheet(self):
        for city in self.destination_data:
            if city['iataCode']:  # Ensure there is a valid IATA code
                new_data = {
                    "price": {
                        "iataCode": city["iataCode"]
                    }
                }
                for attempt in range(5):  # Retry up to 5 times
                    response = requests.put(
                        url=f"{self.get_sheet_data}/{city['id']}",
                        json=new_data,
                        headers=self.auth_header
                    )
                    if response.status_code == 200:
                        print(f"Successfully updated {city['city']}")
                        break
                    elif response.status_code == 429:  # Rate limit exceeded
                        print(f"Rate limit exceeded. Retrying... (attempt {attempt + 1})")
                        time.sleep(2 ** attempt)  # Exponential backoff
                    else:
                        print(f"Failed to update {city['city']}: {response.status_code}, {response.text}")
                        break
            else:
                print(f"No valid IATA code for {city['city']}, skipping update.")
