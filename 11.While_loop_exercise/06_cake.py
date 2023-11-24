width = int(input())
lenght = int(input())

total_pieces = width * lenght
pieces_left = total_pieces
while True:
    pieces = input()
    if pieces == 'STOP':
        print(f'{pieces_left} pieces are left.')
        break
    else:
        pieces_int = int(pieces)
        pieces_left -= pieces_int
        if pieces_left < 0:
            print(f'No more cake left! You need {abs(pieces_left)} pieces more.')
            break




