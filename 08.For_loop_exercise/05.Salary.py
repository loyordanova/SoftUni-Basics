open_tabs = int(input())
salary = float(input())

fine = 0
left = salary

for i in range(1, open_tabs + 1):
    tabs = input()
    if tabs == 'Facebook':
        fine += 150
        left = left - fine
        if left <= 0:
            print(f'You have lost your salary.')
            break

    elif tabs == "Instagram":
        fine += 100
        left = left - fine
        if left <= 0:
            print(f'You have lost your salary.')
            break

    elif tabs == 'Reddit':
        fine += 50
        left = left - fine
        if left <= 0:
            print(f'You have lost your salary.')
            break
    else:
        pass
if left > 0:
    print(int(left))
