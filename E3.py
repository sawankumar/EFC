from urllib import request, error
import argparse
import json
import sys

BASE_API_URL = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = '350f646b3b00e538e31c401debb02bc2'  # Replace with your API key

def read_args():
    parser = argparse.ArgumentParser(description="See the temperature and weather of a city")
    parser.add_argument("city", type=str, help="Input the name of the city")
    return parser.parse_args()

def make_api_url(city_name):
    return f"{BASE_API_URL}?q={city_name}&units=metric&appid={API_KEY}"

def acquire_weather_data(query_api_url):
    try:
        api_response = request.urlopen(query_api_url)
    except error.HTTPError as http_error:
        sys.exit(f"Error: {http_error}")
    weather_data = api_response.read()
    return json.loads(weather_data)

def process_and_output_weather_info(weather_data):
    city_name = weather_data["name"]
    weather_description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]
    pressure = weather_data["main"]["pressure"]
    humidity = weather_data["main"]["humidity"]
    print(f"{city_name.capitalize()}\t"
          f"{weather_description.capitalize()}\t({temperature})°C\t"
          f"Pressure={pressure} \tHumidity={humidity}")

if __name__ == "__main__":
    args = read_args()
    api_query_url = make_api_url(args.city)
    weather_data = acquire_weather_data(api_query_url)
    process_and_output_weather_info(weather_data)
