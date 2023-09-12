month = input()
nights = int(input())

studio = 0
apartment = 0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if 7 < nights < 14:
        studio = studio - studio * 0.05
    elif nights > 14:
        studio = studio - studio * 0.30

elif month == 'June' or month == 'September':
    studio = 75.20
    apartment = 68.70
    if nights > 14:
        studio = studio - studio * 0.20

elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77


if nights > 14:
    apartment = apartment - apartment * 0.10

total = nights * studio
total2 = nights * apartment

print(f'Apartment: {total2:.2f} lv.')
print(f'Studio: {total:.2f} lv.')
