destination = input()
dates = input()
nights_count = int(input())

nights_price = 0
if destination == "France":
    if dates == "21-23":
        nights_price = 30
    elif dates == "24-27":
        nights_price = 35
    elif dates == "28-31":
        nights_price = 40
elif destination == "Italy":
    if dates == "21-23":
        nights_price = 28
    elif dates == "24-27":
        nights_price = 32
    elif dates == "28-31":
        nights_price = 39
elif destination == "Germany":
    if dates == "21-23":
        nights_price = 32
    elif dates == "24-27":
        nights_price = 37
    elif dates == "28-31":
        nights_price = 43

trip_cost = nights_price * nights_count

print(f"Easter trip to {destination} : {trip_cost:.2f} leva.")
