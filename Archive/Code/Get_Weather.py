import requests

# Get current
api = "http://reg.bom.gov.au/fwo/IDQ60901/IDQ60901.95591.json"

response = requests.get(api)
current_data = response.json()
current_data = current_data['observations']["data"]

current = current_data[0]

#Determine a nice day or bad day
def weather_forcast():
	if (current['cloud'] == '-' or current['rain_trace'] == 0.0) and current['gust_kmh'] < 25:
		return True
	else:
		return False

