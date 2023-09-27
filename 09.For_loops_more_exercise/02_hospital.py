period = int(input())

treated = 0
untreated = 0

doctors = 7

for i in range(1, period+ 1):
    patients = int(input())
    if i % 3 != 0:
        if patients <= doctors:
            treated += patients
        else:
            treated += doctors
            untreated += abs(patients - doctors)
    if i % 3 == 0:
        if untreated > treated:
            doctors += 1
        if patients <= doctors:
            treated += patients
        else:
            treated += doctors
            untreated += abs(patients - doctors)

print(f'Treated patients: {treated}.')
print(f'Untreated patients: {untreated}.')


