gasoline = 2.22
diesel = 2.33
gas = 0.93

type_fuel = input()
qty_fuel = float(input())
club_card = input()

if type_fuel == "Gasoline":
    price = qty_fuel * gasoline
    if club_card == 'Yes':
        gasoline = gasoline - 0.18
        price = gasoline * qty_fuel
    if 20 <= qty_fuel <= 25:
        price = price - price * 0.08
    elif qty_fuel > 25:
        price = price - price * 0.1

elif type_fuel == "Diesel":
    price = qty_fuel * diesel
    if club_card == 'Yes':
        diesel = diesel - 0.12
        price = diesel * qty_fuel
    if 20 <= qty_fuel <= 25:
        price = price - price * 0.08
    elif qty_fuel > 25:
        price = price - price * 0.1

elif type_fuel == "Gas":
    price = qty_fuel * gas
    if club_card == 'Yes':
        gas = gas - 0.08
        price = gas * qty_fuel
    if 20 <= qty_fuel <= 25:
        price = price - price * 0.08
    elif qty_fuel > 25:
        price = price - price * 0.1

print(f'{price:.2f} lv.')
