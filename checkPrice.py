# from binance.client import Client


# api_key = 'your-binance-api-key'
# api_secret = 'your-binance-secret-key'

# client = Client(api_key, api_secret)

# # account_info = client.get_account()
# # print(account_info)


# response = client.create_test_order(
#     symbol = 'ETHUSDT',
#     side = 'BUY',
#     type = 'LIMIT',
#     quantity = 0.02,
#     price = 2.134,
#     timeInForce = 'GTC'
#     )

# ticker = client.get_symbol_ticker(symbol=symbol)
# current_price = float(ticker['price'])

# # Calculate the allowed price range based on a percentage (adjust as needed)
# allowed_price_range = current_price * 0.01  # 1% deviation
# valid_price = max(current_price - allowed_price_range, 0)  # Ensure the price is non-negative


# def check_and_execute_trade():
#     symbol = 'ETHUSDT'  # You can choose any trading pair you prefer
#     buy_price = 30000.0  # Set your buy threshold
#     sell_price = 40000.0  # Set your sell threshold
    
#     ticker = client.get_symbol_ticker(symbol=symbol)
#     current_price = float(ticker['price'])
#     print(current_price)
    
#     if current_price < buy_price:
#         print("Buying ETH")
#         buy_order = client.order_market_buy(symbol=symbol, quantity=0.001)  # Adjust quantity as needed

#     elif current_price > sell_price:
#         print("Selling ETH")
#         sell_order = client.order_market_sell(symbol=symbol, quantity=0.001)  # Adjust quantity as needed

# while True:
#     check_and_execute_trade()
#     time.sleep(60)  



from binance.client import Client
import time

api_key = 'your-binance-api-key'
api_secret = 'your-binance-secret-key'
client = Client(api_key, api_secret)

def display_current_price(symbol='ETHUSDT'):
    ticker = client.get_symbol_ticker(symbol=symbol)
    current_price = float(ticker['price'])
    print(f"Current {symbol} Price: {current_price}")

while True:
    display_current_price()
    time.sleep(3)