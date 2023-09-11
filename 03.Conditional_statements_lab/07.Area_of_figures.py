from math import pi

figure = input()

if figure == 'square':
    a = float(input())
    total = a * a
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    total = a * b
elif figure == 'circle':
    r = float(input())
    total = pi * r**2
elif figure == 'triangle':
    a = float(input())
    b = float(input())
    total = (a * b) / 2

print(f'{total:.3f}')


