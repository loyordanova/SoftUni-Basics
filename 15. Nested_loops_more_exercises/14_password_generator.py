n = int(input())
l = int(input())

for num1 in range(1, n +1):
    for num2 in range(1, n +1):
        for num3 in range(97, 97 + l):
            for num4 in range(97, 97 + l):
                for num5 in range(1, n + 1):
                    if num5 > num1 and num5 > num2:
                        print(f'{num1}{num2}{chr(num3)}{chr(num4)}{num5}', end=" ")