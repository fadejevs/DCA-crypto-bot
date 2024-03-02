
# tried to buy into ETH every 3 - 5 seconds depending on the price LOL

from binance.client import Client
import time

api_key = 'your-binance-api-key'
api_secret = 'your-binance-secret-key'
client = Client(api_key, api_secret)

symbol = 'ETHUSDT'
buy_quantity = 0.023  # Updated buy quantity === this is 60 EUR worth of ETH
sell_profit_threshold = 0.40  # Updated sell profit threshold

def display_current_price(symbol='ETHUSDT'):
    ticker = client.get_symbol_ticker(symbol=symbol)
    current_price = float(ticker['price'])
    print(f"Current {symbol} Price: {current_price}")
    return current_price

def place_buy_order(symbol, quantity, price):
    quantity = round(quantity, 5)  # Round to 5 decimal places
    try:
        order = client.create_order(
            symbol=symbol,
            side=Client.SIDE_BUY,
            type=Client.ORDER_TYPE_LIMIT,
            timeInForce=Client.TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=price
        )
        print(f"Buy Order Placed: {order}")
        return True
    except Exception as e:
        print(f"Error placing buy order: {e}")
        return False
        
def place_sell_order(symbol, quantity, price):
    quantity = round(quantity, 5)  # Round to 5 decimal places
    try:
        order = client.create_order(
            symbol=symbol,
            side=Client.SIDE_SELL,
            type=Client.ORDER_TYPE_LIMIT,
            timeInForce=Client.TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=price
        )
        print(f"Sell Order Placed: {order}")
        return True
    except Exception as e:
        print(f"Error placing sell order: {e}")
        return False

def calculate_profit_loss(initial_price, final_price, quantity):
    initial_value = initial_price * quantity
    final_value = final_price * quantity
    profit_loss = final_value - initial_value

    if profit_loss >= 0:
        print(f"Profit: ${profit_loss:.2f}")
    else:
        print(f"Loss: ${abs(profit_loss):.2f}")

def check_price_trend(price_history):
    if price_history[0] > price_history[-1]:
        return 'down'
    elif price_history[0] < price_history[-1]:
        return 'up'
    else:
        return 'stable'

# Initialize price history with the first price
price_history = [display_current_price()]

while True:
    time.sleep(4)
    new_price = display_current_price()
    price_history.append(new_price)

    if len(price_history) > 4:
        price_history.pop(0)  # Keep only the last four prices

        # Calculate the overall price change
        price_change = new_price - price_history[0]

        # down method
        if price_change <= -0.20:
            if place_buy_order(symbol, buy_quantity, new_price):
                while new_price <= price_history[0] + 0.30:  # Wait for 30 cents profit
                    time.sleep(4)
                    new_price = display_current_price()
                place_sell_order(symbol, buy_quantity, new_price)
                calculate_profit_loss(price_history[0], new_price, buy_quantity)
                break  # Exit the loop after selling

        # up method
        elif price_change >= 0.30:
            # Wait for the price to drop back to the value of the first price insert
            while new_price > price_history[0]:
                time.sleep(4)
                new_price = display_current_price()

            # Wait until it drops to the same amount or below the first price insert
            while new_price > price_history[0]:
                time.sleep(4)
                new_price = display_current_price()

            # Check if the price is consistently going down and buy ETH
            if check_price_trend(price_history) == 'down':
                if place_buy_order(symbol, buy_quantity, new_price):
                    while new_price <= price_history[0] + 2:  # Wait for 2 USDT profit
                        time.sleep(4)
                        new_price = display_current_price()
                    place_sell_order(symbol, buy_quantity, new_price)
                    calculate_profit_loss(price_history[0], new_price, buy_quantity)
                    break  # Exit the loop after selling