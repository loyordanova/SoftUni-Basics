budget = float(input())
season = input()

if budget <= 1000:
    stay = 'Camp'
    if season == 'Summer':
        place = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        place = 'Morocco'
        price = budget * 0.45

elif 1000 < budget <= 3000:
    stay = 'Hut'
    if season == 'Summer':
        place = 'Alaska'
        price = budget * 0.80
    elif season == 'Winter':
        place = 'Morocco'
        price = budget * 0.60

elif budget > 3000:
    stay = 'Hotel'
    if season == 'Summer':
        place = 'Alaska'
        price = budget * 0.90
    elif season == 'Winter':
        place = 'Morocco'
        price = budget * 0.90

print(f'{place} - {stay} - {price:.2f}')