import math

magnolies = 3.25
zubbules = 4
roses = 3.50
cactus = 8

number_of_magnolies = int(input())
number_of_zumbules = int(input())
number_of_roses = int(input())
number_of_cactus = int(input())
gift_price = float(input())

total_cash = number_of_magnolies * magnolies + number_of_zumbules * zubbules + number_of_roses * roses + number_of_cactus * cactus

total = total_cash - total_cash * 0.05

if total >= gift_price:
    print(f'She is left with {math.floor(total - gift_price)} leva.')
else:
    print(f'She will have to borrow {math.ceil(gift_price - total)} leva.')
