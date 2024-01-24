type_coffee = input()
suggar = input()
number_of_coffees = int(input())

price = 0
if type_coffee == 'Espresso':
    if suggar == 'Without':
        price = 0.90 * number_of_coffees
    elif suggar == 'Normal':
        price = 1 * number_of_coffees
    elif suggar == 'Extra':
        price = 1.20 * number_of_coffees

if type_coffee == 'Cappuccino':
    if suggar == 'Without':
        price = 1 * number_of_coffees
    elif suggar == 'Normal':
        price = 1.20 * number_of_coffees
    elif suggar == 'Extra':
        price = 1.60 * number_of_coffees

if type_coffee == 'Tea':
    if suggar == 'Without':
        price = 0.50 * number_of_coffees
    if suggar == 'Normal':
        price = 0.60 * number_of_coffees
    if suggar == 'Extra':
        price = 0.70 * number_of_coffees

if suggar == 'Without':
    price = price - price * 0.35

if type_coffee == 'Espresso':
    if number_of_coffees >= 5:
        price = price - price * 0.25

if price > 15:
    price = price - price * 0.20

print(f'You bought {number_of_coffees} cups of {type_coffee} for {price:.2f} lv.')