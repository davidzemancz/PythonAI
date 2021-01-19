from Data import DataCollector
from Base import BaseConfig
from User import User
from binance.client import Client

BaseConfig.load()

if not BaseConfig.is_test():
    print("=============== REALISTIC MODE ===============")
    print("... click to continue")
    input()

login = BaseConfig.get_login()
client = Client(login["api_key"], login["secret_key"])
if BaseConfig.is_test():
    client.API_URL = "https://testnet.binance.vision/api"


print("=============== DATA ===============")
dc = DataCollector(client)
ret = dc.get_data()
if ret.ok:
    print(ret.data)
else:
    print(ret.error)

print("=============== USER ===============")
user = User(client)
ret = user.get()
if ret.ok:
    print(ret.data)
else:
    print(ret.error)

