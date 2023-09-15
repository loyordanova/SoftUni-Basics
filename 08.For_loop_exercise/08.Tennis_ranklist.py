import math

number_of_tournaments = int(input())
starting_points = int(input())

points = starting_points
winning_games = 0

for i in range(1, number_of_tournaments +1):
    stage = input()
    if stage == 'W':
        points += 2000
        winning_games += 1
    elif stage == 'F':
        points += 1200
    elif stage == 'SF':
        points += 720
average_points = (points - starting_points) / number_of_tournaments
percent_won_games = winning_games / number_of_tournaments * 100
print(f'Final points: {points}')
print(f'Average points: {math.floor(average_points)}')
print(f'{percent_won_games:.2f}%')
