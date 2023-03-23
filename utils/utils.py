import requests

def fetch_data(city_name):
    try:
        API_KEY = 'b380c8de2b0fc4c4df8e527f9b746b15'
        
        # fetching data
        data = True
        current_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
        forcast_url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&units=metric'

        # convert to JSON
        current_weather = requests.get(current_url).json()
        forecast = requests.get(forcast_url).json()
        
        if forecast['cod'] == '404':
            data = False
        
        context = {
            'current' : current_weather,
            'forecast' : forecast,
            'data' : data
        }
        
        return context
    
    except Exception as e:
        print(e)

        return {'data' : False}