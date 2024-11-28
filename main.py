from binance.exceptions import BinanceAPIException
import requests
import cbpro
import time
from os import system
import pushover

base_url = "https://api.binance.com/api/v3/ticker/price?symbol="

user_key = "uppfzzq1yx12a3j2rga1z9r1vai5bh"
api_token = "a4bwz8nyw6n3u5reqwx4z483bua9de"


def get_prices(symbol): 
    price = float(requests.get(base_url + symbol).json()['price'])
    return price
    
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   

def send_notification(message):
    """Skickar en notifikation till Pushover"""
    url = 'https://api.pushover.net:443/1/messages.json'
    data = {
        'token': api_token,
        'user': user_key,
        'message': message,
    }
    requests.post(url, data=data)

 
currency = input("Enter A Currency e.g LTCEUR: ")
cprice = float(input("Enter A Price: "))
tecken = input("Up / Down: ")

while True:
    price = get_prices(currency)
    print(f"The current price of {currency} is: {price}")
    if tecken == "Up":
        if price >= cprice:
            send_notification(f"Price of {currency} has reached {price}!")
            print("Price has been reached")
    else:
        if price <= cprice:
            send_notification(f"Price of {currency} has dropped to {price}!")
            print("Price has been reached")
    time.sleep(3)
