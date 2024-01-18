veggi_kg = float(input())
fruits_kg = float(input())
total_veggi_kg = int(input())
total_fruits_kg = int(input())

total = (veggi_kg * total_veggi_kg + fruits_kg * total_fruits_kg)
in_euro = total / 1.94

print(f'{in_euro:.2f}')
