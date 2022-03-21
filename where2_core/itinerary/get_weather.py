import requests

def write_weather_data():
    '''Gets the current weather data'''
    api = "http://reg.bom.gov.au/fwo/IDQ60901/IDQ60901.95591.json"

    #Calls the api and cleans the response
    response = requests.get(api)
    current_data = response.json()
    current_data = current_data['observations']["data"]
    current = current_data[0]

    def weather_forcast():
        ''' Determins if it is a nice day based on weather data '''
        if current['rain_trace'] == 0.0 and current['gust_kmh'] < 35:
            return True
        else:
            return False   
    weather = weather_forcast()

    with open('weather_records.txt', 'a+') as f:
        f.write(f"{weather}\n")

    return weather

def get_weather_data():
    try:
        #Read in weather from within the hour
        with open('weather_records.txt', 'r') as f:
            weather = f.readlines()[-1]
            if 'False' in weather:
                weather = False
            else:
                weather = True
    except FileNotFoundError:
        weather = write_weather_data()

    return weather

