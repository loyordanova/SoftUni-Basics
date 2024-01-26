goals_per_player = 0
hat_trick = False
best_player = ''
while goals_per_player < 10:
    player_name = input()

    if player_name == 'END':
        break

    number_of_goals = int(input())

    if number_of_goals > goals_per_player:
        goals_per_player = number_of_goals
        best_player = player_name

    if number_of_goals >= 10:
        break
print(f'{best_player} is the best player!')

if 3 <= goals_per_player < 10:
    hat_trick = True
    print(f'He has scored {goals_per_player} goals and made a hat-trick !!!')
if goals_per_player >= 10:
    print(f'He has scored {goals_per_player} goals and made a hat-trick !!!')
if goals_per_player < 3:
    print(f'He has scored {goals_per_player} goals.')
