n = int(input())

p1 = []
p2 = []
p3 = []
p4 = []
p5 = []

for i in range(1, n+1):
    num = int(input())
    if num < 200:
        p1.append(num)
    elif num <= 399:
        p2.append(num)
    elif num <= 599:
        p3.append(num)
    elif num <= 799:
        p4.append(num)
    else:
        p5.append(num)

len_p1 = len(p1)
len_p2 = len(p2)
len_p3 = len(p3)
len_p4 = len(p4)
len_p5 = len(p5)

print(f'{len_p1 / n * 100:.2f}%')
print(f'{len_p2 / n * 100:.2f}%')
print(f'{len_p3 / n * 100:.2f}%')
print(f'{len_p4 / n * 100:.2f}%')
print(f'{len_p5 / n * 100:.2f}%')
