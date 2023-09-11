puzzle = 2.60
doll = 3
teddy_bear = 4.10
minion = 8.20
truck = 2

trip_price = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

whole_amount = number_of_puzzles * puzzle + number_of_dolls * doll + number_of_minions * minion + number_of_bears * \
               teddy_bear + number_of_trucks * truck
number_of_toys = number_of_puzzles + number_of_trucks + number_of_minions + number_of_bears + number_of_dolls

if number_of_toys >= 50:
    discount = whole_amount * 0.25
    whole_amount = whole_amount - discount

rent = whole_amount * 0.1
profit = whole_amount - rent

rest = abs(profit - trip_price)

if profit > trip_price:
    print(f"Yes! {rest:.2f} lv left.")
else:
    print(f"Not enough money! {rest:.2f} lv needed.")
