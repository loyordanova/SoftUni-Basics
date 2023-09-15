age = int(input())
washing_machine = float(input())
toy_price = int(input())


money = 0
toys = 0
brother = 0
final_money = 0
for i in range(1, age +1):
    if i % 2 == 0:
        present = final_money + 10
        money += present
        final_money = present
        brother += 1
    else:
        toys += 1

money_toys = toys * toy_price
total_money = money_toys + money - brother

if total_money >= washing_machine:
    print(f'Yes! {total_money - washing_machine:.2f}')
else:
    print(f'No! {washing_machine - total_money:.2f}')


