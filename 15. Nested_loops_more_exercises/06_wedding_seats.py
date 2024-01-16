last_sector = input()
number_of_rows = int(input())
seats_on_odd_row = int(input())

count = 0

for sector in range(65, ord(last_sector) + 1):
    number_of_rows += 1
    for row in range(1, number_of_rows):
        letter = 97
        if row % 2 == 0:
            for seat in range(1, seats_on_odd_row + 3):
                count += 1
                print(f'{chr(sector)}{row}{chr(letter)}')
                letter += 1

        elif row % 2 != 0:
            for seat in range(1, seats_on_odd_row + 1):
                count += 1
                print(f'{chr(sector)}{row}{chr(letter)}')
                letter += 1
print(count)




