number = int(input())

special = []
start = 1111

while start < 10000:
    count = 0
    true = 0

    for index, digit in enumerate(str(start)):
        n = int(digit)
        count += 1
        if n == 0:
            continue
        if number % n == 0:
            true += 1

    if true == 4:
        special.append(start)
    if count == 4:
        start += 1

print(*special)

