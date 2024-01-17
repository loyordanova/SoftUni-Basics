import math
n = int(input())
count = 0
roof = math.floor((n + 1) / 2)
walls = math.floor((n / 2) - 1)
for i in range(1, roof + 1):
    if n % 2 != 0:
        count += 1
        print('*')
        break
    else:
        count += 2
        print('*' * 2)
        break
for x in range(1, roof):
    print('*' * (count + 2))
    count += 2

for y in range(1, walls + 2):
    if n == 2:
        print("|" + "|")
    else:
        print('|' + "*" * (n -2) + "|")
