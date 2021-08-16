import requests
from enum import Enum

class Cripto(Enum):
    BTC = 'bitcoin'
    LINK = 'chainlink'

def request_mercadoBtc(cripto:Cripto):
    """Request in API MercadoBTC for data in today"""
    request = requests.get("https://www.mercadobitcoin.net/api/BTC/day-summary/2020/6/20/")
    return request.json()

# print(request_mercadoBtc('bitcoin'))