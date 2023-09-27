number_of_students = int(input())

top = 0
very_good = 0
good = 0
poor = 0
total = 0

for i in range(1, number_of_students +1):
    grade = float(input())
    total += grade
    if grade < 3:
        poor += 1
    elif 3 <= grade <= 3.99:
        good += 1
    elif 4 <= grade <= 4.99:
        very_good += 1
    else:
        top += 1

average = total / number_of_students
print(f'Top students: {top / number_of_students * 100:.2f}%')
print(f'Between 4.00 and 4.99: {very_good / number_of_students * 100:.2f}%')
print(f'Between 3.00 and 3.99: {good / number_of_students * 100:.2f}%')
print(f'Fail: {poor / number_of_students * 100:.2f}%')
print(f'Average: {average:.2f}')

