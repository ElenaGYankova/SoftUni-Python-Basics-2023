fuel_type = str(input())
litres = float(input())

if fuel_type in ("Diesel", "Gasoline", "Gas"):
    if litres >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")
else:
    print("Invalid fuel!")
