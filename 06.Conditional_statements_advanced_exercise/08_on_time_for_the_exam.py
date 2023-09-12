hour_exam = int(input())
minute_exam = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_total_minutes = hour_exam * 60 + minute_exam
arrival_total_minutes = arrival_hour * 60 + arrival_minute

if arrival_total_minutes > exam_total_minutes:
    print('Late')
elif arrival_total_minutes == exam_total_minutes:
    print('On time')
elif exam_total_minutes - arrival_total_minutes <= 30:
    print(' On time')
else:
    print('Early')

result = abs(exam_total_minutes - arrival_total_minutes)

if exam_total_minutes - arrival_total_minutes > 0:
    if result < 60:
        print(f'{result} minutes before the start')
    else:
        hour = result // 60
        minutes = result % 60
        print(f'{hour}:{minutes:02d} hours before the start')
elif arrival_total_minutes - exam_total_minutes > 0:
    if result < 60:
        print(f'{result} minutes after the start')
    else:
        hour = result // 60
        minutes = result % 60
        print(f'{hour}:{minutes:02d} hours after the start')






