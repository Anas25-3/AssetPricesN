import requests
import time

# Binance and Pushover API configuration
base_url = "https://api.binance.com/api/v3/ticker/price?symbol="
user_key = "uppfzzq1yx12a3j2rga1z9r1vai5bh"
api_token = "ami83swmrzpsdkfftm8sy5vysbep3p"

def get_prices(symbol):
    """Fetches the current price of a cryptocurrency from Binance."""
    try:
        response = requests.get(base_url + symbol)
        response.raise_for_status()
        price = float(response.json()['price'])
        return price
    except requests.exceptions.RequestException as e:
        print(f"Error fetching price for {symbol}: {e}")
        return None

def send_notification(message):
    """Sends a notification to Pushover."""
    url = 'https://api.pushover.net/1/messages.json'
    data = {
        'token': api_token,
        'user': user_key,
        'message': message,
    }
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        result = response.json()
        if result.get('status') == 1:
            print("Notification sent successfully!")
        else:
            print(f"Failed to send notification: {result.get('errors')}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending notification: {e}")

# Define currency pair, target price, and direction (no input needed)
currency = "LTCUSDC"  # Set your currency pair here
cprice = 108.82  # Set your target price here
tecken = "Down"  # Set "Up" or "Down" for alert direction

# Validate direction
if tecken not in ["Up", "Down"]:
    print("Invalid direction. Please enter 'Up' or 'Down'.")
    exit()

print("Starting price monitoring... Press Ctrl+C to stop.")

while True:
    price = get_prices(currency)
    if price is not None:
        print(f"The current price of {currency} is: {price}")

        if tecken == "Up" and price >= cprice:
            send_notification(f"Price of {currency} has reached {price}!")
            print("Price target reached.")
            break
        elif tecken == "Down" and price <= cprice:
            send_notification(f"Price of {currency} has dropped to {price}!")
            print("Price target reached.")
            break
    else:
        print("Skipping this iteration due to API error.")

    time.sleep(3)
