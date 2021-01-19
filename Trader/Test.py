import os
from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor
import json
import csv


# https://testnet.binance.vision/
api_key = "pSZGzFoLUV2namqaIDIXbf1UH9KsekiyMDFJH6kRSMooA0ZaqgNZcPGStMhPKMlL"
secret_key = "y3Hq42MpTuTXjY9izTC5xQgbgwRZiWXchnpPcFQv8HleNNjQQ55JVHw8ZxmKpxSN"

client = Client(api_key, secret_key)
client.API_URL = "https://testnet.binance.vision/api"


#print(client.get_account())
#print(client.get_asset_balance(asset='BTC'))

# get latest price from Binance API
btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
# print full output (dictionary)
print(btc_price)

btc_price = {'error':False}

def btc_trade_history(msg):
    ''' define how to process incoming WebSocket messages '''
    if msg['e'] != 'error':
        print(msg['c'])
        btc_price['last'] = msg['c']
        btc_price['bid'] = msg['b']
        btc_price['last'] = msg['a']
    else:
        btc_price['error'] = True


bsm = BinanceSocketManager(client)
conn_key = bsm.start_symbol_ticker_socket('BTCUSDT', btc_trade_history)
#bsm.start()

# get timestamp of earliest date data is available
timestamp = client._get_earliest_valid_timestamp('BTCUSDT', '1d')
print(timestamp)

bars = client.get_historical_klines('BTCUSDT', '1d', timestamp, limit=1000)

# option 1 - save to file using json method
with open('btc_bars.json', 'w') as e:
    json.dump(bars, e)
print("Json done")

with open('btc_bars.csv', 'w', newline='') as f:
    wr = csv.writer(f)
    for line in bars:
        wr.writerow(line)
print("CSV done")

input()

# stop websocket
bsm.stop_socket(conn_key)

# properly terminate WebSocket
reactor.stop()