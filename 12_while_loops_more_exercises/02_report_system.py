total_sum = int(input())

cash = 0
total_sum_cash = 0
pos = 0
total_sum_pos = 0
transactions = 0
collected_money = 0

while collected_money < total_sum:
    price = input()

    if price == 'End':
        print(f'Failed to collect required money for charity.')
        break

    elif price != 'End':
        price = int(price)
        transactions += 1

        if transactions % 2 != 0:
            if price > 100:
                print(f'Error in transaction!')
            else:
                collected_money += price
                cash += 1
                total_sum_cash += price
                print('Product sold!')
        else:
            if price <= 10:
                print(f'Error in transaction!')
            else:
                collected_money += price
                pos += 1
                total_sum_pos += price
                print('Product sold!')

if collected_money >= total_sum:
    print(f'Average CS: {total_sum_cash / cash:.2f}')
    print(f'Average CC: {total_sum_pos / pos:.2f}')




