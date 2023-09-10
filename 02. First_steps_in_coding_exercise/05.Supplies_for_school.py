pens = 5.80
markers = 7.20
detergent = 1.20

packs_of_pens = int(input())
packs_of_markers = int(input())
liters_of_detergent = int(input())
procent_of_discount = int(input())

price_of_packs_of_pens = packs_of_pens*pens
price_of_packs_of_markers = packs_of_markers*markers
price_of_liters_of_detergent = liters_of_detergent*detergent
total_amount = price_of_liters_of_detergent+price_of_packs_of_markers+price_of_packs_of_pens
discount = procent_of_discount/100

price = discount*total_amount
total = total_amount-price

print(total)
