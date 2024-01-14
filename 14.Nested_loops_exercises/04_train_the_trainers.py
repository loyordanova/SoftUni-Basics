juri_number = int(input())
presentation_name = input()
average_total = 0
total_grades = 0

while presentation_name != 'Finish':
    final_grade = 0

    for grades in range(juri_number):
        grade = float(input())
        final_grade += grade
        average_total += grade
        total_grades += 1

    print(f'{presentation_name} - {final_grade / juri_number:.2f}.')

    presentation_name = input()

print(f"Student's final assessment is {average_total / total_grades:.2f}.")

