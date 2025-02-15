import pandas as pd

coin_list = [
    {"Coin": "Bitcoin", "Ticker": "BTC-USD"},
    {"Coin": "Ethereum", "Ticker": "ETH-USD"},
    {"Coin": "Binance Coin", "Ticker": "BNB-USD"},
    {"Coin": "Ripple", "Ticker": "XRP-USD"},
    {"Coin": "Cardano", "Ticker": "ADA-USD"}
]

dc = pd.DataFrame(coin_list)
print(dc)

