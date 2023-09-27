stadium_capacity = int(input())
number_of_fans = int(input())

A = 0
B = 0
V = 0
G = 0
total_sectors = 0

for fan in range(1, number_of_fans +1):
    total_sectors += 1
    sector = input()
    if sector == 'A':
        A += 1
    if sector == 'B':
        B += 1
    if sector == 'V':
        V += 1
    if sector == 'G':
        G += 1

print(f'{A / total_sectors * 100:.2f}%')
print(f'{B / total_sectors * 100:.2f}%')
print(f'{V / total_sectors * 100:.2f}%')
print(f'{G / total_sectors * 100:.2f}%')
print(f'{total_sectors / stadium_capacity * 100:.2f}%')

