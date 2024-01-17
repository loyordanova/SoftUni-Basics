n = int(input())

for i in range(1, n + 1):
    if i < n:
        print(' ' * (n -i) + '* ' * i)
    if i == n:
        for i in range(n, 0, -1):
            print(' ' * (n -i) + '* ' * i)