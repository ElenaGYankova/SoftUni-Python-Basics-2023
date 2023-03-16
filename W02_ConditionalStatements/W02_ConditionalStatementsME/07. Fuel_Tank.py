fuel_type = input()
litres_in_tank = float(input())

if fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas":
    if litres_in_tank >= 25:
        print(f"You have enough {(fuel_type.lower())}.")
    else:
        print(f"Fill your tank with {(fuel_type.lower())}!")
else:
    print("Invalid fuel!")