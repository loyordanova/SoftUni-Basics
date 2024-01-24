profit = float(input())

price = 0

while profit > price:
    coctail_name = input()

    if coctail_name == 'Party!':

        print(f'We need {profit - price:.2f} leva more.')
        print(f'Club income - {price:.2f} leva.')
        break
    else:
        number_of_coctails = int(input())
        
        coctail_price = len(coctail_name)
        price += coctail_price * number_of_coctails

        if (coctail_price * number_of_coctails) % 2 != 0:
            price -= (coctail_price * number_of_coctails) * 0.25

if price >= profit:
    print(f'Target acquired.')
    print(f'Club income - {price:.2f} leva.')


