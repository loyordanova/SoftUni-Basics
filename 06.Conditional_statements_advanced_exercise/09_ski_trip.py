days = int(input())
place_type = input()
score = input()


room_for_one = 18
apartment = 25
president_apartment = 35

days = days - 1

total_price = 0

if place_type == 'room for one person':
    total_price = days * room_for_one

elif place_type == 'apartment':
    if days < 10:
        price = days * apartment
        total_price = price - price * 0.30
    elif 10 < days < 15:
        price = days * apartment
        total_price = price - price * 0.35
    else:
        price = days * apartment
        total_price = price - price * 0.50

elif place_type == 'president apartment':
    if days < 10:
        price = days * president_apartment
        total_price = price - price * 0.10
    elif 10 < days < 15:
        price = days * president_apartment
        total_price = price - price * 0.15
    else:
        price = days * president_apartment
        total_price = price - price * 0.20

if score == 'positive':
    total_price = total_price + total_price * 0.25
else:
    total_price = total_price - total_price * 0.10

print(f'{total_price:.2f}')




