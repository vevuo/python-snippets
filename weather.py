"""
The OpenWeather API https://openweathermap.org/api

E.g. usage: python weather.py Helsinki

Prints something like:

The weather for Helsinki (lat 60.17 long 24.94):
Temp: 22.82 °C.
Description: clear sky
Humidity: 77 %
Wind: 2 m/s 250° W

After the inital weather requests the script asks for other locations.
"""

import sys
import json
import requests

API_KEY = ''
DIRECTIONS = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]

def call_openweather(location):
	url = 'https://api.openweathermap.org/data/2.5/weather?q=' + location + '&APPID=' + API_KEY + '&units=metric'
	r = requests.get(url)
	if r.status_code > 400:
		print('Location not found or problem with the request.')
		return False
	else:
		return r.json()

def print_weather(name, lat, lon, temp, weather_desc, humidity, wind_speed, wind_direction=None):
	print(f'\nThe weather for { name } (lat { lat } long { lon }):')
	print(f'Temp: { temp } °C.')
	print(f'Description: { weather_desc }')
	print(f'Humidity: { humidity } %')
	if wind_direction is None:
		print(f'Wind: { wind_speed } m/s')
	else:
		print(f'Wind: { wind_speed } m/s { wind_direction }° { get_cardinal_direction(wind_direction) }')

def get_cardinal_direction(wind_direction):
	compass_point = int((wind_direction + 11.25) / 22.5)
	return DIRECTIONS[compass_point % 16]

def main(argv_location):
	while True:
		if argv_location:
			location = str(argv_location)						
			argv_location = None
		else:
			location = input('\nType in a location: ')
			location = location.replace(' ', '%20')
		
		if location is 'q':
			break

		results = call_openweather(location)
		
		if results is not False:
			print_weather(
				results['name'],
				results['coord']['lat'],
				results['coord']['lon'],
				results['main']['temp'],
				results['weather'][0]['description'],
				results['main']['humidity'],
				results['wind']['speed'],
				results['wind']['deg'] if 'deg' in results['wind'] else None,
				)
		
if __name__ == '__main__':
	try:
		if sys.argv[1]:
			main(sys.argv[1])
	except:
		main(None)
