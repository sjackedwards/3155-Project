import requests

def make_api_call(departure_date, origin_place, destination_place, api_key):
    url = "https://skyscanner44.p.rapidapi.com/fly-to-country"

    querystring = {
        "destination": destination_place,
        "origin": origin_place,
        "departureDate": departure_date,
        "currency": "USD",
        "locale": "en-US",
        "country": "US"
    }

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "skyscanner44.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API call failed with status code {response.status_code}")

