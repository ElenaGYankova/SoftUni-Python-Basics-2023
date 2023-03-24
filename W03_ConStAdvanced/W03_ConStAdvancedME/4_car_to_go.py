budget = float(input())
season = input()

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_model = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        car_model = "Jeep"
        price = budget * 0.65
if 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_model = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        car_model = "Jeep"
        price = budget * 0.80
elif budget > 500:
    car_class = "Luxury class"
    car_model = "Jeep"
    price = budget * 0.90

print(f"{car_class}")
print(f"{car_model} - {price:.2f}")
