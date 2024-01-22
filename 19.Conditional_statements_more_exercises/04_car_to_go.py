budget = float(input())
season = input()

if budget <= 100:
    class_car = 'Economy class'
    if season == 'Summer':
        car = 'Cabrio'
        price = budget * 0.35
    elif season == 'Winter':
        car = 'Jeep'
        price = budget * 0.65

elif 100 <= budget <= 500:
    class_car = 'Compact class'
    if season == 'Summer':
        car = 'Cabrio'
        price = budget * 0.45
    elif season == 'Winter':
        car = 'Jeep'
        price = budget * 0.80

elif budget > 500:
    class_car = 'Luxury class'
    car = 'Jeep'
    price = budget * 0.90

print(f'{class_car}')
print(f'{car} - {price:.2f}')
