city = input()
packet_type = input()
vip_discount = input()
days = int(input())
price = 0

if days > 7:
    days -= 1

if city == 'Bansko' or city == 'Borovets':
    if packet_type == 'withEquipment':
        price = days * 100
        if vip_discount == 'yes':
            price = price - price * 0.10
    elif packet_type == 'noEquipment':
        price = days * 80
        if vip_discount == 'yes':
            price = price - price * 0.05

if city == 'Varna' or city == 'Burgas':
    if packet_type == 'withBreakfast':
        price = days * 130
        if vip_discount == 'yes':
            price = price - price * 0.12
    elif packet_type == 'noBreakfast':
        price = days * 100
        if vip_discount == 'yes':
            price = price - price * 0.07

if days < 1:
    print(f'Days must be positive number!')

elif city != 'Varna' and city != 'Burgas' and city != 'Borovets' and city != "Bansko":
    print(f'Invalid input!')

elif packet_type != 'noEquipment' and packet_type != "withEquipment" and packet_type != 'noBreakfast' and packet_type != 'withBreakfast':
    print(f'Invalid input!')

else:
    print(f'The price is {price:.2f}lv! Have a nice time!')
