number_of_floors = int(input())
number_of_rooms = int(input())


for floor in range(number_of_floors, 0,  -1):
    for room in range(0, number_of_rooms):

        if floor % 2 == 0:
            letter = 'O'
        else:
            letter = 'A'
        if floor == number_of_floors:
            letter = 'L'

        print(f'{letter}{floor}{room}', end=" ")
    print( )




