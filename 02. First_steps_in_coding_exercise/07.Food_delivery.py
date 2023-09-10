chicken_menu = 10.35
fish_menu = 12.40
veggi_menu = 8.15

chicken_orders = int(input())
fish_orders = int(input())
veggi_orders = int(input())

price_chichen = chicken_orders*chicken_menu
price_fish = fish_orders*fish_menu
price_veggi = veggi_orders*veggi_menu

total_menu_price = price_veggi+price_fish+price_chichen
dessert = 20/100*total_menu_price

total = total_menu_price+dessert+2.50

print(total)
