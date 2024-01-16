import sys

coins_1_lv = int(input())
coins_2_lv = int(input())
money_5_lv = int(input())
total_sum = int(input())

for sum1 in range(0, coins_1_lv + 1):
    count1 = 1
    for sum2 in range(0, coins_2_lv + 1):
        count2 = 2
        for sum3 in range(0, money_5_lv + 1):
            count3 = 5
            if sum1 * count1 + sum2 * count2 + sum3 * count3 == total_sum:
                print(f"{sum1} * 1 lv. + {sum2} * 2 lv. + {sum3} * 5 lv. = {total_sum} lv.")
