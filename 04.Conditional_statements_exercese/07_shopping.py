budget = float(input())
number_of_video_cards = int(input())
number_of_processors = int(input())
number_of_ram = int(input())

video_card = 250
total_video_cards = video_card * number_of_video_cards
processor = total_video_cards * 0.35
ram = total_video_cards * 0.1

total = total_video_cards + (number_of_processors * processor) + (number_of_ram * ram)

if number_of_video_cards > number_of_processors:
    total = total - (total * 0.15)

if total < budget:
    left = budget - total
    print(f"You have {left:.2f} leva left!")
else:
    more = total - budget
    print(f"Not enough money! You need {more:.2f} leva more!")
