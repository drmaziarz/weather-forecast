import os

import requests
from dotenv import load_dotenv


def configure():
    load_dotenv()


configure()


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?" \
          f"q={place}&" \
          f"appid={os.getenv('API_KEY')}&" \
          f"units=metric"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))
