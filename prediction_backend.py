import requests

API_KEY = "a8a1faca976a4cb582a834f2325410ec"


def get_data(place, days=None):
    api_url = f'http://api.openweathermap.org/data/2.5/forecast?' \
              f'q={place}&' \
              f'appid={API_KEY}'
    response = requests.get(api_url)
    data = response.json()
    filtered_data = data['list']
    num_of_values = 8*days
    filtered_data = filtered_data[:num_of_values]
    return filtered_data


if __name__ == '__main__':
    print(get_data(place='Tokyo', days=3))
