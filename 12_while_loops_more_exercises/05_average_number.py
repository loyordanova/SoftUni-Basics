n = int(input())

roll = 0
average = 0

while roll < n:
    num = int(input())
    roll += 1
    average += num

print(f'{average / n:.2f}')
