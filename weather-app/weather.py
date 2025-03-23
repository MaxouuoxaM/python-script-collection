import requests
import sys

API_KEY = ""
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'fr'
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        name = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        wind = data['wind']['speed']

        print(f"\n📍 {name}, {country}")
        print(f"🌡 Température : {temp}°C")
        print(f"☁️ Ciel : {desc}")
        print(f"💨 Vent : {wind} km/h")
    else:
        print("❌ Ville non trouvée ou erreur d'API.")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        city = " ".join(sys.argv[1:])
        get_weather(city)
    else:
        print("⚠️  Utilisation : python weather.py [nom_de_ville]")
