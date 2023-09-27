number_of_cargo = int(input())

total_kg = 0
microbus = 0
truck = 0
train = 0
for i in range(1, number_of_cargo +1):
    cargo_kg = int(input())
    total_kg += cargo_kg
    if cargo_kg <= 3:
        microbus += cargo_kg
    elif 4 <= cargo_kg <= 11:
        truck += cargo_kg
    else:
        train += cargo_kg

average = (microbus * 200 + truck * 175 + train * 120) / total_kg
with_microbus = microbus / total_kg * 100
with_truck = truck / total_kg * 100
with_train = train / total_kg * 100

print(f'{average:.2f}')
print(f'{with_microbus:.2f}%')
print(f'{with_truck:.2f}%')
print(f'{with_train:.2f}%')


