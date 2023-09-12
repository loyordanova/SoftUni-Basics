budget = float(input())
season = input()

price = 0
country = ""
place = ""

if budget <= 100 and season == "summer":
    country = "Bulgaria"
    price = budget * 0.30
elif budget <= 100 and season == "winter":
    country = "Bulgaria"
    price = budget * 0.70

if 100 < budget <= 1000 and season == "summer":
    price = budget * 0.40
    country = "Balkans"
elif 100 < budget <= 1000 and season == "winter":
    country = "Balkans"
    price = budget * 0.80

if budget > 1000:
    country = "Europe"
    price = budget * 0.90

if season == "summer":
    place = "Camp"
    if season == "summer" and budget > 1000:
        place = "Hotel"
elif season == "winter":
    place = "Hotel"

print(f"Somewhere in {country}")
print(f"{place} - {price:.2f}")
