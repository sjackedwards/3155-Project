import requests

# TODO 1: Lets implements # of people flying in adults parameter.
def get_flight_destinations(api_key, origin, destination, departure_date, return_date, adults):
    
    currency="USD"
    country_code="US" 
    market="en-US"
    
    url = "https://skyscanner50.p.rapidapi.com/api/v1/searchFlights"

    querystring = {
        "origin": origin,
        "destination": destination,
        "date": departure_date,
        "returnDate": return_date,
        "adults": adults,
        "currency": currency,
        "countryCode": country_code,
        "market": market
    }

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "skyscanner50.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()


def search_airport(city_name):
    url = "https://skyscanner50.p.rapidapi.com/api/v1/searchAirport"

    querystring = {"query": city_name}
    print(querystring)
    headers = {
        "X-RapidAPI-Key": "3c7f94a4ecmsh378ff346ebadb4cp1f88a0jsnd9fae43f43e4",
        "X-RapidAPI-Host": "skyscanner50.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response_data = response.json()
    return response_data["data"][0].get("PlaceId")

