from Base import BaseActionResult, BaseConfig
from binance.client import Client

class User:
    def __init__(self, client):
        self.client = client

    def get(self):
        try:
            ret = {}

            #ret = self.client.get_asset_balance(asset='BTC')
            ret = self.client.get_account()

            return BaseActionResult(True, "", ret)
        except BaseException as err:
            return BaseActionResult(False, str(err), err)