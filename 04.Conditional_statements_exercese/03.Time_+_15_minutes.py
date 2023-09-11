hour = int(input())
minutes = int(input())
total_minutes = minutes + 15
total_hour = hour + total_minutes

if total_minutes >= 60:
    total_minutes = total_minutes % 60
    add_minutes = (minutes+15) // 60
    total_hour = hour + add_minutes
else:
    total_hour = hour

if total_minutes == 60:
    total_minutes = 00

if total_hour > 24:
    total_hour = total_hour // 24

if total_hour == 24:
    total_hour = 0

if total_minutes < 10:
    print (f"{total_hour}:0{total_minutes}")
else:
    print(f"{total_hour}:{total_minutes}")
