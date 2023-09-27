hour = 0
minutes = 0
seconds = 0

for i in range(0, 24):
    hour = i
    if hour > 24:
        hour = 0
    for i in range(0, 60):
        minutes = i
        if minutes > 59:
            minutes = 0
            hour += 1
        for y in range(0, 60):
            seconds = y
            if seconds > 59:
                seconds = 0
                minutes += 1
            print(f'{hour} : {minutes} : {seconds}')
