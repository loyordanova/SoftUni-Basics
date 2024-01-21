import math

n = int(input())
word = input()
tax = 0

if n < 20:
    if word == 'day':
        tax += 0.7 + 0.79 * n
    elif word == 'night':
        tax += 0.7 + 0.90 * n
elif 20 <= n < 100:
    if word == 'night' or word == 'day':
        tax += 0.09 * n
elif 100 <= n:
    if word == 'day' or word == 'night':
        tax += 0.06 * n
print(f'{tax:.2f}')