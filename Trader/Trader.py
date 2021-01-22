import sys
from Base import BaseActionResult
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException

class Trader:
    def __init__(self, client = None):
        self.client = client

    def buy(self) -> BaseActionResult:
        try:
            ret = None

            try:
                buy_limit = self.client.create_test_order(
                    symbol='ETHUSDT',
                    side='BUY',
                    type='LIMIT',
                    timeInForce='GTC',
                    quantity=100,
                    price=200)

            except BinanceAPIException as e:
                print(e)
            except BinanceOrderException as e:
                print(e)


            return BaseActionResult(True, "", ret)
        except BaseException as err:
            return BaseActionResult(False, str(err), err)


        