first_letter = input()
second_letter = input()
third_letter = input()

count = 0

first_letter = ord(first_letter)
second_letter = ord(second_letter)
third_letter = ord(third_letter)

for first in range(first_letter, second_letter + 1):
    for second in range(first_letter, second_letter + 1):
        for third in range(first_letter, second_letter + 1):

            if first != third_letter and second != third_letter and third != third_letter:
                count += 1
                print(f'{chr(first)}{chr(second)}{chr(third)}', end=" ")
print(count, end="")

