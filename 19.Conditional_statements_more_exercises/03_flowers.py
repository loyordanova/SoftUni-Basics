chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
day_type = input()

price = 0

if season == 'Spring' or season == 'Summer':
    price += chrysanthemums * 2
    price += roses * 4.10
    price += tulips * 2.50
elif season == 'Autumn' or season == 'Winter':
    price += chrysanthemums * 3.75
    price += roses * 4.50
    price += tulips * 4.15

if day_type == 'Y':
    price = price + price * 0.15

if season == 'Spring' and tulips >= 7:
    price = price - price * 0.05
if season == 'Winter' and roses >= 10:
    price = price - price * 0.10
if roses + chrysanthemums + tulips >= 20:
    price = price - price * 0.20

total = price + 2

print(f'{total:.2f}')