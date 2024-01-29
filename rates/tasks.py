import requests


def get_currency_rates():
    url = "https://api.exchangerate-api.com/v4/latest/RUB"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError({"error": response.json()})
    rates = response.json().get("rates")
    return rates.get("USD"), response.json().get("date")
