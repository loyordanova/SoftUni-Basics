town = input()
sales = float(input())

list1 = ['Sofia', 'Varna', 'Plovdiv']

if town in list1 and 0 <= sales <= 500:
    if town == 'Sofia':
        result = sales * 5 / 100
    elif town == 'Varna' and 0 <= sales <= 500:
        result = sales * 4.5 / 100
    elif town == 'Plovdiv' and 0 <= sales <= 500:
        result = sales * 5.5 / 100
    print(f'{result:.2f}')


elif town in list1 and 500 <= sales <= 1000:
    if town == 'Sofia':
        result = sales * 7 / 100
    elif town == 'Varna' and 500 <= sales <= 1000:
        result = sales * 7.5 / 100
    elif town == 'Plovdiv' and 500 <= sales <= 1000:
        result = sales * 8 / 100
    print(f'{result:.2f}')

elif town in list1 and 1000 <= sales <= 10000:
    if town == 'Sofia':
        result = sales * 8 / 100
    elif town == 'Varna' and 1000 <= sales <= 10000:
        result = sales * 10 / 100
    elif town == 'Plovdiv' and 1000 <= sales <= 10000:
        result = sales * 12 / 100
    print(f'{result:.2f}')


elif town in list1 and sales > 10000:
    if town == 'Sofia':
        result = sales * 12 / 100
    elif town == 'Varna' and sales > 10000:
        result = sales * 13 / 100
    elif town == 'Plovdiv' and sales > 10000:
        result = sales * 14.5 / 100
    print(f'{result:.2f}')
else:
    print('error')






