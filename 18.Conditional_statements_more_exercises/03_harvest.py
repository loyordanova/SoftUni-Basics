import math

x = int(input())
y = float(input())
z = int(input())
workers = int(input())

total_vineyard = x * y
for_wine = (total_vineyard * 0.4) / 2.5

if for_wine >= z:
    print(f'Good harvest this year! Total wine: {math.floor(for_wine)} liters.')
    print(f'{math.ceil(for_wine - z)} liters left -> {(math.ceil((for_wine - z) / workers))} liters per person.')
else:
    print(f'It will be a tough winter! More {math.floor(z - for_wine)} liters wine needed.')