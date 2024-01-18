mackerel = float(input())
sprinkle = float(input())
bonito_kg = float(input())
safrit_kg = float(input())
clams_kg = float(input())

bonito = mackerel + mackerel * 0.6
safrit = sprinkle + sprinkle * 0.8
clams = 7.5 * clams_kg

total = bonito * bonito_kg + safrit * safrit_kg + clams
print(f'{total:.2f}')

