start = int(input())
final = int(input())
magic_number = int(input())

combinations = 0
comb1 = 0
for i in range(start, final + 1):
    for x in range(start, final + 1):
        combinations += 1

        if i + x == magic_number:
            comb1 += 1
            num1 = i
            num2 = x
            if comb1 == 1:
                print(f'Combination N:{combinations} ({num1} + {num2} = {magic_number})')
                break
if comb1 == 0:
    print(f'{combinations} combinations - neither equals {magic_number}')

