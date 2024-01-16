start_range = int(input())
end_range = int(input())
magic_number = int(input())

combinations = 0
first_part_number = 0
second_part_number = 0
flag = False

for num in range(start_range, end_range + 1):
    for num1 in range(start_range, end_range + 1):
        combinations += 1
        if flag:
            break
        if num + num1 == magic_number:
            combinations_new = combinations
            first_part_number = num
            second_part_number = num1
            flag = True
if flag:
    print(f'Combination N:{combinations_new} ({first_part_number} + {second_part_number} = {magic_number})')
else:
    print(f'{combinations} combinations - neither equals {magic_number}')