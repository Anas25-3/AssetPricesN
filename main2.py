from binance.exceptions import BinanceAPIException

import requests
import cbpro
import time
from os import system

base_url = "https://api.binance.com/api/v3/ticker/price?symbol="

def get_prices(symbol): 
    price = float(requests.get(base_url + symbol).json()['price'])
    return price
    """return price['price']"""
 
currency = input("Enter A Currency e.g LTCEUR: ")
cprice = float(input("Enter A Price: "))
tecken = input("Up / Down: ")

while True:
    price = get_prices(currency)
    print(f"The current price of {currency} is: {price}")
    if tecken == "Up":
        if price >= cprice:
            print("Price has been reached")
    else:
        if price <= cprice:
            print("Price has been reached")
    time.sleep(3)