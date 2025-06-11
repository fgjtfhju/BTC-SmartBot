from binance.client import Client
import os

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

client = Client(API_KEY, API_SECRET)

DOGE_PAIR = "DOGEBTC"
SOL_PAIR = "SOLBTC"
BTC_HAVEN = "BTC"

def run_bot():
    balance = float(client.get_asset_balance(asset='BTC')['free'])

    selected_pair = DOGE_PAIR
    if is_solana_trending_better():
        selected_pair = SOL_PAIR

    if balance > 0.00005:
        try:
            order = client.order_market_buy(
                symbol=selected_pair,
quoteOrderQty = str(round(balance * 0.8, 6))
                
            )
            print("Kjøpte:", order)
            print("20 % beholdes som BTC-havn.")
        except Exception as e:
            print("Feil ved kjøp:", str(e))

def is_solana_trending_better():
    sol_price = float(client.get_symbol_ticker(symbol=SOL_PAIR)['price'])
    doge_price = float(client.get_symbol_ticker(symbol=DOGE_PAIR)['price'])
    return sol_price > doge_price
