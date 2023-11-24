goal = 0

while 10000 > goal:
    steps = input()

    if steps == 'Going home':
        steps = input()
        steps_int = int(steps)
        goal += steps_int
        break
    else:
        steps_int = int(steps)
        goal += steps_int

if 10000 > goal:
    print(f'{abs(10000 - goal)} more steps to reach goal.')

if goal > 10000:
    print(f'Goal reached! Good job!')
    print(f'{abs(goal - 10000)} steps over the goal!')









