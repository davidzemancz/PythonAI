import random

file = open("btc.csv")
file.readline()


def get_unit_price(prev_price):
    global dispersion, file

    #unit_price = random.randint(max(prev_price - dispersion, 0), prev_price + dispersion)

    arr = file.readline().split(",")
    if len(arr) == 1:
        return -1
    unit_price = float(arr[2])
    
    return unit_price

def buy(unit_price, amount):
    global wallet, assets
    
    price = amount * unit_price
    
    if price > wallet: # Pokud nemam dost, nakoupim za zbytek
        amount = wallet / unit_price
        price = amount * unit_price
    
    wallet -= price
    assets += amount

def sell(unit_price, amount):
    global wallet, assets

    if amount > assets: # Pokud nemam dost, prodam vse
        amount = assets

    wallet += amount * unit_price
    assets -= amount

def get_purchase_avarange():
    global history
    total_price = 0
    total_amount = 0
    for item in history:
        total_price += item[0] * item[1]
        total_amount += item[1]
    return total_price / total_amount


wallets = []
total = 0

for i in range(100):
    dispersion = 5
    wallet = 10_000_000
    assets = 10
    purchase_avarange = 10_000 # Prumerna cena nakupu
    unit_price = 50 # Vychozi cena
    amount = 10
    history = []

    for j in range(100):
        unit_price = get_unit_price(unit_price)
        if unit_price == -1:
            break

        if unit_price < purchase_avarange:
            buy(unit_price, amount)
            history.append((unit_price, amount))
            purchase_avarange = get_purchase_avarange()
        elif unit_price > purchase_avarange:
            sell(unit_price, amount)

    unit_price = 10_000 # get_unit_price(unit_price)
    sell(unit_price, assets)
        
    wallets.append(wallet - 10_000_000)
    total += wallet - 10_000_000

    print("RUN:", i)

profit = 0
for wallet in wallets:
    if wallet > 0: profit += 1
    else: profit -= 1
    print("WALLET:", wallet)

print("TOTAL:", total)
print("PROFIT:", str(profit) + "/100")