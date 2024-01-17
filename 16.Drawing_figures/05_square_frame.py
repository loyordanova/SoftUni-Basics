n = int(input())

n1 = n - 2
print('+', "- " * n1 + '+')
for i in range(2, n):
    print('|', '- ' * n1 + '|')

print('+', "- " * n1 + '+')