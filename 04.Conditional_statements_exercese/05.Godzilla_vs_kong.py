movie_budget = float(input())
number_statist = int(input())
costume_price = float(input())

decor = movie_budget * 0.1

costumes = costume_price * number_statist
total = decor + costumes

if number_statist >= 150:
    discount = costume_price * 0.1
    new_price = costume_price - discount
    costume = new_price * number_statist
    total = decor + costume

if total > movie_budget:
    more = total - movie_budget
    print(f"Not enough money!")
    print(f"Wingard needs {more:.2f} leva more.")

else:
    left = movie_budget - total
    print(f"Action!")
    print(f"Wingard starts filming with {left:.2f} leva left.")
