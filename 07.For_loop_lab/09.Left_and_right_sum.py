n = int(input())

left = 0
right = 0

for i in range(n):
    num = int(input())
    left += num

for x in range(n):
    num = int(input())
    right += num

if left == right:
    print(f'Yes, sum = {left}')
else:
    diff = abs(right - left)
    print(f'No, diff = {diff}')
