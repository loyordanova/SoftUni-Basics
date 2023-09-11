score = int(input())
bonus = 0
if score <= 100:
    bonus = 5
elif score <= 1000:
    bonus = 0.2 * score
else:
    bonus = 0.1 * score
if score % 2 == 0:
    bonus = bonus + 1
if score % 10 == 5:
    bonus = bonus + 2

print(bonus)
print(score + bonus)