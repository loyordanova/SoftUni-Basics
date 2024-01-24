budget = float(input())
stays = int(input())
price_per_night = float(input())
add_money_percent = int(input())

money_for_stay = stays * price_per_night
if stays >= 7:
    price_per_night = price_per_night - price_per_night * 0.05
    money_for_stay = stays * price_per_night
add_money = budget * add_money_percent / 100
total = add_money + money_for_stay

if budget >= total:
    print(f'Ivanovi will be left with {budget - total:.2f} leva after vacation.')
else:
    print(f'{total - budget:.2f} leva needed.')
