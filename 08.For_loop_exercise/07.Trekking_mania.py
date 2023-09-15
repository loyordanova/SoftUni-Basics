number_of_groups = int(input())

musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
total_ppl = 0

for i in range(1, number_of_groups +1):
    people = int(input())
    if people <= 5:
        musala += people
        total_ppl += people
    elif 6 <= people <= 12:
        monblan += people
        total_ppl += people
    elif 12 <= people <= 25:
        kilimandjaro += people
        total_ppl += people
    elif 26 <= people <= 40:
        k2 += people
        total_ppl += people
    elif people >= 41:
        everest += people
        total_ppl += people

print(f'{musala / total_ppl * 100:.2f}%')
print(f'{monblan / total_ppl * 100:.2f}%')
print(f'{kilimandjaro / total_ppl * 100:.2f}%')
print(f'{k2 / total_ppl * 100:.2f}%')
print(f'{everest / total_ppl * 100:.2f}%')
