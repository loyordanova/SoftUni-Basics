actor_name = input()
academy_points = float(input())
number_of_jury = int(input())

points = academy_points

for i in range(number_of_jury):
    name_of_jury = input()
    jury_points = float(input())
    add_points = len(name_of_jury) * (jury_points / 2)
    points += add_points
    if points >= 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!')
        break
    else:
        pass

if points < 1250.5:
    print(f'Sorry, {actor_name} you need {abs(1250.5 - points):.1f} more!')


