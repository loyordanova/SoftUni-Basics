age = float(input())
gender = input()

if gender == 'm'  and age >= 16:
    result = 'Mr.'
elif gender == 'm' and age < 16:
    result = 'Master'
elif gender == 'f' and age >= 16:
    result = 'Ms.'
elif gender == 'f' and age < 16:
    result = 'Miss'

print(result)