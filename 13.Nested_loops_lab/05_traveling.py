collected_money = 0

while True:
    place = input()

    if place == 'End':
        break

    budget = float(input())

    while collected_money < budget:
        saved_money = float(input())
        collected_money += saved_money

    if collected_money >= budget:
        print(f'Going to {place}!')
        collected_money = 0




