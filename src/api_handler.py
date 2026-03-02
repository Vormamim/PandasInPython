"""
API Handler Module
Simple functions to fetch JSON data from free APIs or load samples.
"""

import json
import requests

# Supported APIs for tutorials
APIS = {
    "openmeteo": {
        "name": "Open-Meteo (Weather Data)",
        "description": "Free weather data API - no authentication required",
        "base_url": "https://api.open-meteo.com/v1",
        "endpoints": {
            "forecast": "/forecast"
        }
    }
}

    
def fetch_weather(latitude, longitude, timezone="auto"):
    """
    Fetch weather forecast data from Open-Meteo API.

    Args:
        latitude (float): Location latitude
        longitude (float): Location longitude
        timezone (str): Timezone for data

    Returns:
        dict: Weather response
    """
    url = f"{APIS['openmeteo']['base_url']}/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,relative_humidity_2m,precipitation",
        "timezone": timezone,
        "forecast_days": 7
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
    
def display_raw_data(data, max_items=5):
    """Display raw API response in formatted way."""
    if not data:
        print("No data to display")
        return
    
    if isinstance(data, list):
        print(f"\n[List with {len(data)} items]")
        print("First few items:")
        for i, item in enumerate(data[:max_items]):
            print(f"\n--- Item {i+1} ---")
            if isinstance(item, dict):
                for key, value in item.items():
                    print(f"  {key}: {value}")
            else:
                print(f"  {item}")
        if len(data) > max_items:
            print(f"\n... and {len(data) - max_items} more items")
            
    elif isinstance(data, dict):
        print("\n[Dictionary]")
        for key, value in data.items():
            if isinstance(value, (list, dict)):
                print(f"  {key}: <{type(value).__name__} with {len(value)} items>")
            else:
                print(f"  {key}: {value}")
    
def list_available_apis():
    """List the weather API as the only option."""
    print("\n[INFO] Available API: Open-Meteo weather data")
    print("-" * 60)
    print("  https://api.open-meteo.com/v1/forecast")



# Test function
if __name__ == "__main__":
    # show available APIs
    list_available_apis()

    print("\n" + "="*60)
    print("Testing Open-Meteo Weather API")
    print("="*60)

    weather = fetch_weather(-33.8688, 151.2093)
    if weather:
        display_raw_data(weather, max_items=1)
