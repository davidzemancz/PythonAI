from Base import BaseActionResult, BaseConfig
from binance.client import Client

class DataCollector:
    def __init__(self, client = None):
        self.client = client

    def get_data(self) -> BaseActionResult:
        try:
            ret = {}

            ret = {"BTCBUSD": self.client.get_symbol_ticker(symbol="BTCBUSD")}

            return BaseActionResult(True, "", ret)
        except BaseException as err:
            return BaseActionResult(False, str(err), err)
       
