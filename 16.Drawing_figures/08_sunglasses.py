import math

n = int(input())

n1 = n * 2

print('*' * n1 + ' ' * n + '*' * n1)
for i in range(1, n - 1):
    if i != math.ceil((n / 2) - 1) and n != 3:
        print('*' + '/' * (n1 - 2) + '*' + " " * n + "*" + '/' * (n1 - 2) + '*')
    if i == math.ceil((n / 2) - 1) or n == 3:
        print('*' + '/' * (n1 - 2) + '*' + "|" * n + "*" + '/' * (n1 - 2) + '*')
print('*' * n1 + ' ' * n + '*' * n1)