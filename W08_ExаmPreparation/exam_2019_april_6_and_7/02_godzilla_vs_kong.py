budget = float(input())
extras_count = int(input())
extras_clothing_price = float(input())

decor = budget * 0.10

if extras_count >= 150:
    extras_clothing_price -= 0.10 * extras_clothing_price

extras = extras_count * extras_clothing_price
total = extras + decor
diff = abs(budget - total)

if budget < total:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
