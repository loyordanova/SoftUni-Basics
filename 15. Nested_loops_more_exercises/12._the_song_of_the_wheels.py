number = int(input())

count = 0

a1 = 0
b1 = 0
c1 = 0
d1 = 0

for a in range(1, 10):
    for b in range(1, 10):
        if a < b:
            for c in range(1, 10):
                for d in range(1, 10):
                    if c > d:
                        if (a * b) + (c * d) == number:
                            print(f'{a}{b}{c}{d}', end=" ")
                            count += 1
                            if count == 4:
                                a1 = a
                                b1 = b
                                c1 = c
                                d1 = d
if count >= 4:
    print(f"")
    print(f'Password: {a1}{b1}{c1}{d1}')
if count < 4:
    print(f"")
    print(f'No!')