money = input()
balance = 0
while money != 'NoMoreMoney':
    total = float(money)

    if total < 0:
        print(f'Invalid operation!')
        break
    balance += total
    print(f'Increase: {total:.2f}')
    money = input()
print(f'Total: {balance:.2f}')


