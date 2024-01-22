season = input()
km_per_month = float(input())

if season == 'Spring' or season == "Autumn":
    if km_per_month <= 5000:
        salary = 0.75 * km_per_month
    elif 5000 < km_per_month <= 10000:
        salary = 0.95 * km_per_month
    elif 10000 < km_per_month <= 20000:
        salary = 1.45 * km_per_month

elif season == 'Summer':
    if km_per_month <= 5000:
        salary = 0.90 * km_per_month
    elif 5000 < km_per_month <= 10000:
        salary = 1.10 * km_per_month
    elif 10000 < km_per_month <= 20000:
        salary = 1.45 * km_per_month

elif season == 'Winter':
    if km_per_month <= 5000:
        salary = 1.05 * km_per_month
    elif 5000 < km_per_month <= 10000:
        salary = 1.25 * km_per_month
    elif 10000 < km_per_month <= 20000:
        salary = 1.45 * km_per_month

for_4_months = salary * 4
total = for_4_months - for_4_months * 0.1

print(f'{total:.2f}')