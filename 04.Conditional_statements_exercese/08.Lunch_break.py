import math
name = str(input())
episod_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
rest_time = break_time / 4
left_time = break_time - (lunch_time + rest_time)

if left_time >= episod_time:
    left = math.ceil(left_time - episod_time)
    print(f"You have enough time to watch {name} and left with {left} minutes free time.")
else:
    more = math.ceil(episod_time - left_time)
    print(f"You don't have enough time to watch {name}, you need {more} more minutes. ")
