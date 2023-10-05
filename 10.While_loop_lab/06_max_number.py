import sys

number = input()
max = -sys.maxsize

while number != 'Stop':
    num = int(number)
    if num > max:
        max = num
    number = input()
print(f'{max}')
