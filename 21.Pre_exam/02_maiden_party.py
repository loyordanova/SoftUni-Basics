total_cost = float(input())
love_quotes = int(input())
wax_roses = int(input())
keyholders = int(input())
caricatures = int(input())
lucky_sup = int(input())

quotes = love_quotes * 0.60
rose = wax_roses * 7.20
key = keyholders * 3.60
cari = caricatures * 18.20
luck = lucky_sup * 22

total_price = quotes + rose + key + cari + luck
total_number = love_quotes + wax_roses + keyholders + caricatures + lucky_sup

if total_number >= 25:
    total_price = total_price - total_price * 0.35
hosting_tax = total_price * 0.1
total_price = total_price - hosting_tax

if total_price >= total_cost:
    print(f'Yes! {total_price - total_cost:.2f} lv left.')
else:
    print(f'Not enough money! {total_cost - total_price:.2f} lv needed.')
