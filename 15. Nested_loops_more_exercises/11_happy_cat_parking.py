days = int(input())
hours = int(input())

total_tax = 0
for day in range(1, days + 1):
    tax = 0
    for t in range(1, hours + 1):
        if t == 24:
            t = 0
        if day % 2 == 0:
            if t % 2 != 0:
                tax += 2.50
                total_tax += 2.50
            else:
                tax += 1
                total_tax += 1
        if day % 2 != 0:
            if t % 2 == 0:
                tax += 1.25
                total_tax += 1.25
            else:
                tax += 1
                total_tax += 1

    print(f'Day: {day} - {tax:.2f} leva')
print(f'Total: {total_tax:.2f} leva')