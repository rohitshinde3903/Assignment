import requests

API_KEY = 'ab9b3b194417f47d190230e94730638b'
LOCATION = 'Pune'
url = f'http://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={API_KEY}&units=metric'

response = requests.get(url)
data = response.json()
print(data)
