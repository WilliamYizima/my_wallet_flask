import requests
from enum import Enum
import datetime
import json

from wallet.ext.api.services.model import Gain

class Cripto(Enum):
    """The endpoint support 2 types of crypto"""
    bitcoin = 'BTC'
    chainlink = 'LINK'

def request_mercadoBtc(cripto:Cripto,n_day_past:int=0)->list:
    """Request in API MercadoBTC for data yesterday(default)

    Args:
        cripto (Cripto): [type of cripto: bitcoin or chainlink]
        n_day_past (int): [past days , 0 = yesterday]
    """
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=n_day_past+1)
    
    date_today_for_url = f"{yesterday.year}/{yesterday.month}/{yesterday.day}"
    coin = Cripto[cripto].value
    
    request = requests.get(
                            f'https://www.mercadobitcoin.net/api/{coin}/day-summary/{date_today_for_url}/'
                            )
    response = request.json()
    [closing , date] = response['closing'], response['date']
    return [closing , date]

def bulk_insert_db(cripto:Cripto, n_data:int = 3 )-> dict:
    """get data in api and return quantity:n_data 

    Args:
        cripto (Cripto): [type of cripto: bitcoin or chainlink]
        n_data (int): [quantity last days]
    return dict
    """
    list_cripto_data = []
    for i in range(n_data):
        amount, date = request_mercadoBtc(cripto=cripto, 
                                    n_day_past=(i))
        # transform in datetime ->for dataclass
        # formatted_date = datetime.datetime.strptime(date, '%Y-%m-%d')

        gain_request = Gain(description=cripto,
                            amount=amount,
                            date=date)
        list_cripto_data.append(gain_request)
        
    return {'result':list_cripto_data}