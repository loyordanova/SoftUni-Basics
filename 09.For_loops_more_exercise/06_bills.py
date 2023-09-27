months = int(input())

total_months = 0
total_electricity = 0
others = 0
for month in range(1, months + 1):
    electicity = float(input())
    total_months += 1
    total_electricity += electicity
    others += 20 + 15 + electicity + (20 + 15 + electicity) * 0.20

total_water = 20 * total_months
total_net = 15 * total_months

print(f'Electricity: {total_electricity:.2f} lv')
print(f'Water: {total_water:.2f} lv')
print(f'Internet: {total_net:.2f} lv')
print(f'Other: {others:.2f} lv')
print(f'Average: {(total_electricity + total_water + total_net + others) / total_months:.2f} lv')
