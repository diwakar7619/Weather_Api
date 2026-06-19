from weather_functions import get_coordinates, get_weather

city = input("Enter city: ")

coordinates = get_coordinates(city)

if coordinates is None:
    print("City not found.")

else:
    lat, lon = coordinates

    temperature, time = get_weather(lat, lon)
    print("=" * 25)
    print(" Weather App ")
    print("=" * 25)

    print(f"City: {city}")
    print(f"Temperature: {temperature} °C")
    print(f"Time: {time}")
