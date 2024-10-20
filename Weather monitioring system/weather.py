import requests
from config import API_KEY, CITIES, API_URL
from datetime import datetime

def get_weather_data():
    weather_data = []
    for city in CITIES:
        response = requests.get(f"{API_URL}?q={city}&appid={API_KEY}")
        if response.status_code == 200:
            weather_data.append(response.json())
    return weather_data

def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15

def process_weather_data(data):
    processed_data = []
    for item in data:
        city = item['name']
        main = item['weather'][0]['main']
        temp = kelvin_to_celsius(item['main']['temp'])
        feels_like = kelvin_to_celsius(item['main']['feels_like'])
        dt = datetime.utcfromtimestamp(item['dt']).strftime('%Y-%m-%d %H:%M:%S')

        processed_data.append({
            "city": city,
            "main": main,
            "temp": temp,
            "feels_like": feels_like,
            "timestamp": dt
        })
    return processed_data

def summarize_daily_weather(data):
    summary = {
        "avg_temp": sum([d['temp'] for d in data]) / len(data),
        "max_temp": max([d['temp'] for d in data]),
        "min_temp": min([d['temp'] for d in data]),
        "dominant_condition": get_dominant_weather_condition(data)
    }
    return summary

def get_dominant_weather_condition(data):
    conditions = [d['main'] for d in data]
    return max(set(conditions), key=conditions.count)
