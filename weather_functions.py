import requests


def get_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    response = requests.get(url)

    data = response.json()

    results = data.get("results")

    if results is None:
        return None

    latitude = results[0]["latitude"]
    longitude = results[0]["longitude"]

    return latitude, longitude
    return None


def get_weather(latitude, longitude):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m"
    )
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data["current"]["temperature_2m"]
        time = data["current"]["time"]

        return temperature, time
    return None
