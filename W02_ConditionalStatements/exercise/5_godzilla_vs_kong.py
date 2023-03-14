budget = float(input())
extras = int(input())
costume = float(input())

costume_price = extras * costume
decor = budget * 0.1

if extras > 150:
    costume_price *= 0.9

diff = abs(budget - (decor + costume_price))

if decor + costume_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")