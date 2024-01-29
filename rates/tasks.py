import requests


def get_currency_rates(base_currency: str):
    url = "https://api.exchangerate-api.com/v4/latest/%s" % base_currency

    response = requests.get(url)
    print(response.json())
    if response.status_code != 200:
        raise ValueError({"error": response.json()})
    return response.json()
