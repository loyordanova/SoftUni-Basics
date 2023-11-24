money_for_vacation = float(input())
available_money = float(input())

money_left = available_money
spend = 0
days = 0

while money_left < money_for_vacation and spend < 5:
    action = input()
    money_saved_or_spend = float(input())
    days += 1

    if action == 'spend':
        spend += 1
        money_left -= money_saved_or_spend
        if money_left < 0:
            money_left = 0

    elif action == 'save':
        money_left += money_saved_or_spend
        spend = 0

if spend == 5:
    print(f"You can't save the money.")
    print(f'{days}')

else:
    print(f'You saved the money for {days} days.')









