import math

two_leva = 0
lev = 0
fifty = 0
twenty = 0
ten = 0
five = 0
two = 0
one = 0

while True:
    money = float(input())
    rest_money = money
    if rest_money >= 2:
        two_leva += rest_money // 2
        rest_money = round((rest_money % 2) ,2)
    if 1 <= rest_money < 2:
        lev += rest_money // 1
        rest_money = round((rest_money % 1), 2)
    if 0.50 <= rest_money < 1:
        fifty += rest_money // 0.50
        rest_money = round((rest_money % 0.50), 2)
    if 0.20 <= rest_money < 0.50:
        twenty += rest_money // 0.20
        rest_money = round((rest_money % 0.20), 2)
    if 0.10 <= rest_money < 0.20:
        ten += rest_money // 0.10
        rest_money = round((rest_money % 0.10), 2)
    if 0.05 <= rest_money < 0.10:
        five += rest_money // 0.05
        rest_money = round((rest_money % 0.05), 2)
    if 0.02 <= rest_money < 0.05:
        two += rest_money // 0.02
        rest_money = round((rest_money % 0.02) , 2)
    if 0.01 <= rest_money < 0.02:
        one += 1
    break

total = two_leva + lev + fifty + twenty + ten + five + two + one
print(int(total))

