# Weather App

A simple Python Weather App that uses the Open-Meteo API to fetch real-time weather information for any city.

## Features

- Search weather by city name
- Fetch latitude and longitude automatically
- Display current temperature
- Display current weather timestamp
- Handle invalid city names gracefully

## Technologies Used

- Python
- Requests
- Open-Meteo Geocoding API
- Open-Meteo Weather API

## Project Structure

weather_app/

├── main.py

├── weather_functions.py

├── README.md

└── pyproject.toml

## How It Works

1. User enters a city name.
2. The Geocoding API returns latitude and longitude.
3. The Weather API uses those coordinates.
4. Current temperature and time are extracted.
5. Results are displayed in the terminal.

## Example Output

```text
Enter city: Jodhpur

=========================
 Weather App
=========================
City: Jodhpur
Temperature: 35.8 °C
Time: 2026-06-19T13:00
```

## API Endpoints Used

Geocoding:

https://geocoding-api.open-meteo.com/v1/search

Weather:

https://api.open-meteo.com/v1/forecast

## Author

Pratham Diwakar