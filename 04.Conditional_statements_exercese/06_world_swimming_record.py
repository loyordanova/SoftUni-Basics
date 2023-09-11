import math

sec = float(input())
meters = float(input())
time = float(input())

new_record = meters * time
water = (math.floor(meters / 15)) * 12.5
total_time = new_record + water

if sec < total_time:
    slower = total_time - sec
    print(f"No, he failed! He was {slower:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")