import sys

number = input()
min = sys.maxsize

while number != 'Stop':
    num = int(number)
    if num < min:
        min = num
    number = input()
print(f'{min}')
