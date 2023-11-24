width = int(input())
length = int(input())
height = int(input())

apartment_size = width * length * height
total_boxes = 0

while True:
    boxes = input()

    if boxes == 'Done':
        print(f'{abs(apartment_size - total_boxes)} Cubic meters left.')
        break

    if boxes != 'Done':
        boxes = int(boxes)
        total_boxes += boxes

        if total_boxes >= apartment_size:
            total_boxes -= apartment_size
            print(f'No more free space! You need {abs(total_boxes)} Cubic meters more.')
            break
