a = int(input())
b = int(input())
max_generated_passwords = int(input())

combinations = 0
rotation = 0
flag = False

for pass1 in range(35, 55):
    for pass2 in range(64, 96):
        for pass3 in range(1, a + 1):
            for pass4 in range(1, b + 1):
                combinations += 1
                if combinations > max_generated_passwords:
                    break
                print(f'{chr(pass1)}{chr(pass2)}{pass3}{pass4}{chr(pass2)}{chr(pass1)}', end="|")
                if pass3 == a and pass4 == b:
                    flag = True
                    break
                pass1 += 1
                if pass1 > 55:
                    pass1 = 35

                pass2 += 1
                if pass2 > 96:
                    pass2 = 64
            if flag:
                break
        if flag:
            break
    if flag:
        break

