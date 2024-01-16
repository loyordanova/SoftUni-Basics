number = int(input())

for num1 in range(1, number):
    if num1 <= 9:
        for num2 in range(1, number):
            if num2 <= 9:
                for num3 in range(1, number):
                    if num3 <= 9:
                        for num4 in range(1, number):
                            if num4 <= 9:
                                if num1 + num2 == num3 + num4:
                                    if number % (num1 + num2) == 0 and number % (num3 + num4) == 0:
                                        print(f'{num1}{num2}{num3}{num4}', end=" ")