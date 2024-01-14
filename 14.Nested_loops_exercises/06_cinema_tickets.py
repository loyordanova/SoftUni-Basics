movie_name = input()


total_student = 0
total_standard = 0
total_kid = 0
total_tickets = 0

while movie_name != "Finish":
    free_seats = int(input())
    total = 0
    ticket_type = input()
    while ticket_type != "End":
        total_tickets += 1
        total += 1

        if ticket_type == 'standard':
            total_standard += 1
        elif ticket_type == 'student':
            total_student += 1
        elif ticket_type == 'kid':
            total_kid += 1

        if total == free_seats:
            break

        ticket_type = input()

    full = total / free_seats * 100
    print(f'{movie_name} - {full:.2f}% full.')
    movie_name = input()

print(f'Total tickets: {total_tickets}')
print(f'{total_student / total_tickets * 100:.2f}% student tickets.')
print(f'{total_standard / total_tickets * 100:.2f}% standard tickets.')
print(f'{total_kid / total_tickets * 100:.2f}% kids tickets.')
