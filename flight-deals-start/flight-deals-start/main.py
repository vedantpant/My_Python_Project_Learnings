from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

# Fetch the data from the Google Sheet
sheet_data = data_manager.get_destination_data()

# Update IATA codes where they are missing
for row in sheet_data:
    if row["iataCode"] == "":
        iata_code = flight_search.get_destination_code(row['city'])
        if iata_code is not None:
            row["iataCode"] = iata_code
            print(f"Updated {row['city']} with IATA code: {iata_code}")
        else:
            print(f"Could not retrieve IATA code for city: {row['city']}")

# Print the updated data for verification
print(sheet_data)

# Update the DataManager's destination_data and push changes back to the Google Sheet
data_manager.destination_data = sheet_data
data_manager.put_data_in_sheet()
