import requests

API_KEY = "a8a1faca976a4cb582a834f2325410ec"


def get_data(place, days=None, weather_report=None):
    api_url = f'http://api.openweathermap.org/data/2.5/forecast?' \
              f'q={place}&' \
              f'appid={API_KEY}'
    response = requests.get(api_url)
    data = response.json()
    filtered_data = data['list']
    num_of_values = 8*days
    filtered_data = filtered_data[:num_of_values]
    if weather_report == 'Temperature':
        filtered_data = [dict["main"]['temp'] for dict in filtered_data]

    if weather_report == 'Sky':
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
    return filtered_data


if __name__ == '__main__':
    print(get_data(place='Tokyo', days=3, weather_report='Temperature'))
