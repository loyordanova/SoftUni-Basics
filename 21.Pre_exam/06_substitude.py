k = int(input())
l = int(input())
m = int(input())
n = int(input())

number_of_changes = 0
flag = False

for num1 in range(k, 9):
    for num2 in range(9, l - 1, -1):
        for num3 in range(m, 9):
            for num4 in range(9, n - 1, -1):

                if num1 % 2 == 0 and num3 % 2 == 0 and num2 % 2 != 0 and num4 % 2 != 0:
                    first = f'{num1}{num2}'
                    second = f'{num3}{num4}'

                    if first == second:
                        print(f'Cannot change the same player.')
                    else:
                        number_of_changes += 1
                        print(f'{first} - {second}')
                        if number_of_changes >= 6:
                            flag = True
                if flag:
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        break

