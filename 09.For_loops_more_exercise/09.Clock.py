hour = 0
minutes = 0

for i in range(0, 24):
    hour = i
    if hour > 23:
        hour = 0
    for x in range(0, 60):
        minutes = x
        if minutes > 59:
            minutes = 0
            hour += 1
        print(f'{hour} : {minutes}')



