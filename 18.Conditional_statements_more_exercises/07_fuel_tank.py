text = input()
number = float(input())

if text == "Diesel" or text == 'Gasoline' or text == "Gas":
    if number >= 25:
        print(f"You have enough {text.lower()}.")
    else:
        print(f'Fill your tank with {text.lower()}!')
else:
    print(f'Invalid fuel!')

