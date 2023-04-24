drink = input()
sugar = input()
count = int(input())

drink_price = 0

if drink == "Espresso":
    if sugar == "Without":
        drink_price = 0.90
    elif sugar == "Normal":
        drink_price = 1.00
    elif sugar == "Extra":
        drink_price = 1.20
elif drink == "Cappuccino":
    if sugar == "Without":
        drink_price = 1.00
    elif sugar == "Normal":
        drink_price = 1.20
    elif sugar == "Extra":
        drink_price = 1.60
elif drink == "Tea":
    if sugar == "Without":
        drink_price = 0.50
    elif sugar == "Normal":
        drink_price = 0.60
    elif sugar == "Extra":
        drink_price = 0.70

if sugar == "Without":
    drink_price -= 0.35 * drink_price

if drink == "Espresso" and count >= 5:
    drink_price -= 0.25 * drink_price

drink_total = drink_price * count

if drink_total > 15:
    drink_total -= 0.20 * drink_total

print(f"You bought {count} cups of {drink} for {drink_total:.2f} lv.")
