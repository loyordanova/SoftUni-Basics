men = int(input())
women = int(input())
max_table = int(input())

combinations = 0

for comb1 in range(1, men + 1):
    if combinations == max_table:
        break
    for comb2 in range(1, women+ 1):
        combinations += 1
        print(f'({comb1} <-> {comb2})', end=" ")
        if combinations == max_table:
            break



