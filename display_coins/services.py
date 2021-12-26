import requests


def get_coins():
    url = ('https://api.coingecko.com/api/v3/coins/markets?vs_currency'
           '=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false')
    r = requests.get(url)
    data = r.json()
    return data
