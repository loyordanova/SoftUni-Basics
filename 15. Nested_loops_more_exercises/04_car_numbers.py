starting_range = int(input())
ending_range = int(input())

for num1 in range(starting_range, ending_range + 1):
    for num2 in range(starting_range, ending_range +1):
        for num3 in range(starting_range, ending_range + 1):
            for num4 in range(starting_range, ending_range + 1):
                if num1 > num4:
                    if (num2 + num3) % 2 == 0:
                        if num1 % 2 == 0 and num4 % 2 != 0:
                            print(f'{num1}{num2}{num3}{num4}', end=" ")
                        elif num1 % 2 != 0 and num4 % 2 == 0:
                            print(f'{num1}{num2}{num3}{num4}', end=" ")

