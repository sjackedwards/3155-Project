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
