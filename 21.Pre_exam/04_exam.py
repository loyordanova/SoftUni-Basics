number_of_students = int(input())

top_students = 0
between_4_and_5 = 0
between_3_and_4 = 0
fail = 0
all_grades = 0
for student in range(1, number_of_students + 1):
    grade = float(input())
    all_grades += grade
    if grade >= 5:
        top_students += 1
    elif 4.00 <= grade <= 4.99:
        between_4_and_5 += 1
    elif 3.00 <= grade <= 3.99:
        between_3_and_4 += 1
    else:
        fail += 1

top = top_students / number_of_students * 100
very_good = between_4_and_5 / number_of_students * 100
good = between_3_and_4 / number_of_students * 100
faill = fail / number_of_students * 100

average = all_grades / number_of_students

print(f'Top students: {top:.2f}%')
print(f'Between 4.00 and 4.99: {very_good:.2f}%')
print(f'Between 3.00 and 3.99: {good:.2f}%')
print(f'Fail: {faill:.2f}%')
print(f'Average: {average:.2f}')