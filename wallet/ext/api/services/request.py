import requests
from enum import Enum
import datetime
import json

from wallet.ext.api.services.model import Gain

class Cripto(Enum):
    """The endpoint support 2 types of crypto"""
    bitcoin = 'BTC'
    chainlink = 'LINK'

def request_mercadoBtc(cripto:Cripto,n_day_past:int=1):
    """Request in API MercadoBTC for data yesterday

    Args:
        cripto (Cripto): [type of cripto: bitcoin or chainlink]
    """
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=n_day_past)
    
    date_today_for_url = f"{yesterday.year}/{yesterday.month}/{yesterday.day}"
    coin = Cripto[cripto].value
    
    request = requests.get(
                            f'https://www.mercadobitcoin.net/api/{coin}/day-summary/{date_today_for_url}/'
                            )
    response = request.json()
    data = json.dumps(response)
    # closing , date = response.closing, response.date
    # return closing , date
    return data

def bulk_insert_db(cripto:Cripto, n_data:int = 3 ):
    """get data in api and return quantity:n_data 

    Args:
        cripto (Cripto): [type of cripto: bitcoin or chainlink]
        n_data (int): [quantity last days]
    """
    list_cripto_data = []
    for i in range(n_data):

        request = request_mercadoBtc(cripto=cripto, 
                                    n_day_past=n_data)
        gain_request = Gain(description=cripto,
                            amount=request.closing)
        
    return request_mercadoBtc()