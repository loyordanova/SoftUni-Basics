fruit = input()
day = input()
qty = float(input())


weekend = ['Saturday', 'Sunday']
working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
fruits = ['banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes']

if day in working_days and fruit in fruits:
    if fruit == 'banana':
        fruit = 2.50
    elif fruit == 'apple':
        fruit = 1.20
    elif fruit == 'orange':
        fruit = 0.85
    elif fruit == 'grapefruit':
        fruit = 1.45
    elif fruit == 'kiwi':
        fruit = 2.70
    elif fruit == 'pineapple':
        fruit = 5.50
    elif fruit == 'grapes':
        fruit = 3.85
    result = qty * fruit
    print(f'{result:.2f}')

elif day in weekend and fruit in fruits:
    if fruit == 'banana':
        fruit = 2.70
    elif fruit == 'apple':
        fruit = 1.25
    elif fruit == 'orange':
        fruit = 0.90
    elif fruit == 'grapefruit':
        fruit = 1.60
    elif fruit == 'kiwi':
        fruit = 3.00
    elif fruit == 'pineapple':
        fruit = 5.60
    elif fruit == 'grapes':
        fruit = 4.20
    result = qty * fruit
    print(f'{result:.2f}')

else:
    print('error')