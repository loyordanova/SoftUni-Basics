number_of_people = int(input())
season = input()

if season == 'spring':
    if number_of_people <= 5:
        price = number_of_people * 50
    else:
        price = number_of_people * 48

elif season == 'summer':
    if number_of_people <= 5:
        price = number_of_people * 48.50
    else:
        price = number_of_people * 45

elif season == 'autumn':
    if number_of_people <= 5:
        price = number_of_people * 60
    else:
        price = number_of_people * 49.50

elif season == 'winter':
    if number_of_people <= 5:
        price = number_of_people * 86
    else:
        price = number_of_people * 85

if season == 'summer':
    price = price - price * 0.15
if season == 'winter':
    price = price + price * 0.08

print(f'{price:.2f} leva.')