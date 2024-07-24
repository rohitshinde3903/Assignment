import requests
import time
import sqlite3
from datetime import datetime

API_KEY = 'use_your_own_api_key'
LOCATION = 'Pune'

def fetch_weather_data(API_KEY, LOCATION):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    
    print(data) #Printed data to to debug and check the data presentation in console
    if 'main' in data and 'wind' in data: # Handle cases where 'main' or 'wind' keys might be missing
        return {
            'timestamp': datetime.now(),
            'temperature': data['main'].get('temp', None),
            'humidity': data['main'].get('humidity', None),
            'wind_speed': data['wind'].get('speed', None),
            'sunrise_time': data['sys'].get('sunrise', None)
        }
    else:
        print("Error: 'main' or 'wind' key not found in the API response")
        return None

def main():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather (
                        timestamp TEXT,
                        temperature REAL,
                        humidity REAL,
                        wind_speed REAL,
                        sunrise_time REAL)''')
    
    while True:
        data = fetch_weather_data(API_KEY, LOCATION)
        if data:
            cursor.execute('INSERT INTO weather (timestamp, temperature, humidity, wind_speed, sunrise_time) VALUES (?, ?, ?, ?, ?)',
                           (data['timestamp'], data['temperature'], data['humidity'], data['wind_speed'], data['sunrise_time']))
            conn.commit()
            print(f"Data recorded at {data['timestamp']}")
        else:
            print("No data to record")
        
        time.sleep(3600)  # 3600 hundred seconds means 1 hour

if __name__ == '__main__':
    main()
