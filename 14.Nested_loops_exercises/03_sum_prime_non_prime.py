command = input()

sum_prime = 0
sum_non_prime = 0

while command != 'stop':
    command = int(command)

    if command < 0:
        print(f'Number is negative.')
        command = input()
        continue
    count = 0

    for i in range(1, command + 1):
        if command % i == 0:
            count += 1

    if count == 2:
        sum_prime += command
    else:
        sum_non_prime += command

    command = input()

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')


