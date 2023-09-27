number = int(input())

result = 0
second = 0
third = 0
forth = 0
fifth = 0
sixth = 0
seventh= 0

for i in range(1, number + 1):
    n = int(input())
    if n in range(0, 10):
        points = n * 0.20
        result += points
        second += 1
    if n in range(10, 20):
        points = n * 0.30
        result += points
        third += 1
    if n in range(20, 30):
        points = n * 0.40
        result += points
        forth += 1
    if n in range(30, 40):
        result += 50
        fifth += 1
    if n in range(40, 51):
        result += 100
        sixth += 1
    if n < 0 or n > 50:
        result /= 2
        seventh += 1
total_numbers = second + third + forth + fifth + sixth + seventh
print(f'{result:.2f}')
print(f'From 0 to 9: {second / total_numbers * 100:.2f}%')
print(f'From 10 to 19: {third / total_numbers * 100:.2f}%')
print(f'From 20 to 29: {forth / total_numbers * 100:.2f}%')
print(f'From 30 to 39: {fifth / total_numbers * 100:.2f}%')
print(f'From 40 to 50: {sixth / total_numbers * 100:.2f}%')
print(f'Invalid numbers: {seventh / total_numbers * 100:.2f}%')
