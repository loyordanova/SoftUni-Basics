free_days = int(input())

work_days = 365 - free_days
play_time_working_day = work_days * 63
play_time_free_day = free_days * 127
total_play_time = play_time_free_day + play_time_working_day

if total_play_time > 30000:
    hours = (total_play_time - 30000) // 60
    minutes = (total_play_time - 30000) % 60
    print(f'Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    hours = (30000 - total_play_time ) // 60
    minutes = (30000 - total_play_time) % 60
    print(f'Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')