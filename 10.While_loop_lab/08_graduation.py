name = input()
bad_grade = 0
group = 0
total_grades = 0
while True:
    grade = float(input())
    group += 1
    if grade < 4:
        bad_grade += 1

        if bad_grade == 2:
            print(f'{name} has been excluded at {group} grade')
            break
        group -= 1

    else:
        total_grades += grade
    if group == 12:
        print(f'{name} graduated. Average grade: {total_grades / group:.2f}')
        break

