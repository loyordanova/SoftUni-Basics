bad_grades_limit = int(input())

score = 0
problems = 0
last_task = 0
bad_grades = 0
while True:
    task_name = input()
    if task_name == 'Enough':
        print(f'Average score: {score / problems:.2f}')
        print(f'Number of problems: {problems}')
        print(f'Last problem: {last_task}')
        break

    grade = int(input())

    if grade <= 4:
        bad_grades += 1

    if bad_grades >= bad_grades_limit:
        print(f'You need a break, {bad_grades} poor grades.')
        break

    problems += 1
    score += grade
    last_task = task_name
