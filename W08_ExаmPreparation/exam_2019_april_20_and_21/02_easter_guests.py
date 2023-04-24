from math import ceil

number_of_guests = int(input())
budget = int(input())

price_per_easter_bread = 4
price_per_egg = 0.45

easter_bread_bought = ceil(number_of_guests / 3)
eggs_bought = number_of_guests * 2

total = easter_bread_bought * price_per_easter_bread + eggs_bought * price_per_egg
difference = abs(total - budget)
if total <= budget:
    print(f"Lyubo bought {easter_bread_bought} Easter bread and {eggs_bought} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")

'''
from math import ceil

guests = int(input())
budget = int(input())

easter_bread_count = ceil(guests / 3)
easter_bread_cost = easter_bread_count * 4

eggs_count = guests * 2
eggs_cost = eggs_count * 0.45

total_cost = easter_bread_cost + eggs_cost

balance = budget - total_cost

if balance >= 0:
    print(f"Lyubo bought {easter_bread_count} Easter bread and {eggs_count} eggs.\n"
          f"He has {balance:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.\n"
          f"He needs {abs(balance):.2f} lv. more.")
'''