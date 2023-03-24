season = input()
km_for_month = float(input())

if km_for_month <= 5000:
    if season in "Spring" "Autumn":
        price = (km_for_month * 0.75) * 4
    elif season == "Summer":
        price = (km_for_month * 0.90) * 4
    elif season == "Winter":
        price = (km_for_month * 1.05) * 4
if 5000 < km_for_month <= 10000:
    if season in "Spring" "Autumn":
        price = (km_for_month * 0.95) * 4
    elif season == "Summer":
        price = (km_for_month * 1.10) * 4
    elif season == "Winter":
        price = (km_for_month * 1.25) * 4
if 10000 < km_for_month <= 20000:
    if season in "Spring" "Autumn" "Summer" "Winter":
        price = (km_for_month * 1.45) * 4

salary = price * 0.90

print(f"{salary:.2f}")
