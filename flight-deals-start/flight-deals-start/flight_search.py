import requests
import time

amadeus_api_key = "9BmIarHgIQYlXo5GMIqsifNoiQGZ45L5"
amadeus_api_secret = "4raxyAMqoxAVGMrK"
amadeus_api_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"

header_link = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

amadeus_city_search_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations"


class FlightSearch:

    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.amadeus_header = None
        self.amadeus_city_param = None
        self.city_name = None
        self.body = None
        self.header = None
        self._api_key = amadeus_api_key
        self._api_secret = amadeus_api_secret
        self._token = self.get_new_token()
        self.amadeus_city_search_endpoint = amadeus_city_search_endpoint
        self.amadeus_get_api = amadeus_city_search_endpoint

    def get_new_token(self):
        self.header = header_link

        self.body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }

        response = requests.post(url=amadeus_api_endpoint, data=self.body, headers=self.header)
        token_data = response.json()
        access_token = token_data["access_token"]
        return access_token

    def get_destination_code(self, city_name):
        self.city_name = city_name
        self.amadeus_city_param = {
            'subType': 'CITY',
            'keyword': self.city_name
        }
        headers = {
            'Authorization': f'Bearer {self._token}'
        }

        attempt = 0
        while attempt < 5:
            api_response = requests.get(url=f"{self.amadeus_city_search_endpoint}",
                                        params=self.amadeus_city_param, headers=headers)

            if api_response.status_code == 200:
                data = api_response.json()
                if data['data']:  # Check if the data list is not empty
                    city_code = data['data'][0]['iataCode']
                    print(f"IATA Code for {self.city_name}: {city_code}")
                    return city_code
                else:
                    print(f"No data found for city: {self.city_name}")
                    return None
            elif api_response.status_code == 429:
                print("Rate limit exceeded. Retrying...")
                time.sleep(2 ** attempt)  # Exponential backoff
                attempt += 1
            else:
                print("Error in API call:", api_response.json())
                return None

        print("Max retries reached. Could not retrieve IATA code.")
        return None
