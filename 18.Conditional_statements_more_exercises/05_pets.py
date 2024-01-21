import math
number_of_days = int(input())
food_left = int(input())
daily_dog_food = float(input())
daily_cat_food = float(input())
daily_turtle_food = float(input())

dog_needed_food = daily_dog_food * number_of_days
cat_needed_food = daily_cat_food * number_of_days
turtle_needed_food = (daily_turtle_food / 1000) * number_of_days

total_needed_food = dog_needed_food + cat_needed_food + turtle_needed_food
if food_left > total_needed_food:
    print(f'{math.floor(food_left - total_needed_food)} kilos of food left.')
else:
    print(f'{math.ceil(total_needed_food - food_left)} more kilos of food are needed.')
