degrees = int(input())
time_of_day = input()

if time_of_day == 'Morning' and 10 <= degrees <= 18:
    print(f"It's {degrees} degrees, get your Sweatshirt and Sneakers.")
elif time_of_day == 'Morning' and 18 < degrees <= 24:
    print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
elif time_of_day == 'Morning' and degrees >= 25:
    print(f"It's {degrees} degrees, get your T-Shirt and Sandals.")

elif time_of_day == 'Afternoon' and 10 < degrees <= 18:
    print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
elif time_of_day == 'Afternoon' and 18 < degrees <= 24:
    print(f"It's {degrees} degrees, get your T-Shirt and Sandals.")
elif time_of_day == 'Afternoon' and degrees >= 25:
    print(f"It's {degrees} degrees, get your Swim Suit and Barefoot.")

elif time_of_day == 'Evening' and 10 < degrees <= 18:
    print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
elif time_of_day == 'Evening' and 18 < degrees <= 24:
    print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
elif time_of_day == 'Evening' and degrees  >= 25:
    print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
