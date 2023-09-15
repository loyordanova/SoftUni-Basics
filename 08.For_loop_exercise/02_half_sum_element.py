import sys

n = int(input())

max = -sys.maxsize
sum = 0

for i in range(n):
    num = int(input())
    sum += num
    if num > max:
        max = num

if max == sum - max:
    print('Yes')
    print(f'Sum = {max}')
else:
    print('No')
    others = sum - max
    print(f'Diff = {abs(max - others)}')


