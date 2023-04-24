budget = float(input())
gender = input()
age = int(input())
sport = input()

card_price = 0
if sport == "Gym":
    if gender == "m":
        card_price = 42
    elif gender == "f":
        card_price = 35
elif sport == "Boxing":
    if gender == "m":
        card_price = 41
    elif gender == "f":
        card_price = 37
elif sport == "Yoga":
    if gender == "m":
        card_price = 45
    elif gender == "f":
        card_price = 42
elif sport == "Zumba":
    if gender == "m":
        card_price = 34
    elif gender == "f":
        card_price = 31
elif sport == "Dances":
    if gender == "m":
        card_price = 51
    elif gender == "f":
        card_price = 53
elif sport == "Pilates":
    if gender == "m":
        card_price = 39
    elif gender == "f":
        card_price = 37

if age <= 19:
    card_price -= 0.20 * card_price

diff = budget - card_price

if diff > 0:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${abs(diff):.2f} more.")
