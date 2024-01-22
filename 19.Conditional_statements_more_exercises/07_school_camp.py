season = input()
type_of_group = input()
number_of_students = int(input())
number_of_stays = int(input())

if season == 'Winter':
    if type_of_group == 'girls' or type_of_group == 'boys':
        price = 9.60 * number_of_students * number_of_stays
    elif type_of_group == 'mixed':
        price = 10 * number_of_students * number_of_stays
    if type_of_group == 'girls':
        sport = 'Gymnastics'
    elif type_of_group == 'boys':
        sport = 'Judo'
    elif type_of_group == 'mixed':
        sport = 'Ski'

if season == 'Spring':
    if type_of_group == 'girls' or type_of_group == 'boys':
        price = 7.20 * number_of_students * number_of_stays
    elif type_of_group == 'mixed':
        price = 9.50 * number_of_students * number_of_stays
    if type_of_group == 'girls':
        sport = 'Athletics'
    elif type_of_group == 'boys':
        sport = 'Tennis'
    elif type_of_group == 'mixed':
        sport = 'Cycling'

if season == 'Summer':
    if type_of_group == 'girls' or type_of_group == 'boys':
        price = 15 * number_of_students * number_of_stays
    elif type_of_group == 'mixed':
        price = 20 * number_of_students * number_of_stays
    if type_of_group == 'girls':
        sport = 'Volleyball'
    elif type_of_group == 'boys':
        sport = 'Football'
    elif type_of_group == 'mixed':
        sport = 'Swimming'

if number_of_students >= 50:
    price = price - price * 0.5
elif 20 <= number_of_students < 50:
    price = price - price * 0.15
elif 10 <= number_of_students < 20:
    price = price - price * 0.05

print(f'{sport} {price:.2f} lv.')