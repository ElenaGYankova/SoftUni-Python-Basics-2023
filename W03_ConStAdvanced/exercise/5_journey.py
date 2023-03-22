budget = float(input())
season = input()

destination = "Bulgaria" or "Balkans" or "Europe"
type = "Camp" or "Hotel"

price = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.3
        type = "Camp"
    elif season == "winter":
        price = budget * 0.7
        type = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.4
        type = "Camp"
    elif season == "winter":
        price = budget * 0.8
        type = "Hotel"
elif budget > 1000:
    destination = "Europe"
    price = budget * 0.9
    type = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type} - {price:.2f}")
