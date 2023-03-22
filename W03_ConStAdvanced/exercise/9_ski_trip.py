days_stay = int(input())
room_type = input()
review = input()

nights = days_stay - 1
price = 0
total_price = 0
if room_type == "room for one person":
    price = 18

if room_type == "apartment" and nights < 10:
    price = 25 * 0.70
elif room_type == "apartment" and 10 >= nights <= 15:
    price = 25 * 0.50
elif room_type == "apartment" and nights > 15:
    price = 25 * 0.50

if room_type == "president apartment" and nights < 10:
    price = 35 * 0.90
elif room_type == "president apartment" and 10 >= nights <= 15:
    price = 35 * 0.85
elif room_type == "president apartment" and nights > 15:
    price = 35 * 0.80

if review == "positive":
    price *= 1.25
elif review == "negative":
    price *= 0.90

final_price = nights * price
print(f"{final_price:.2f}")

'''
days_stay = int(input())
room_type = input()
review = input()

nights = days_stay - 1
price = 0
p_room = 18
p_apartment = 25
p_president = 35
if room_type == "room for one person":
    price = p_room
elif room_type == "apartment":
    price = p_apartment
    if nights < 10:
        price *= 0.70
    elif 10 >= nights <= 15:
        price *= 0.65
    elif nights > 15:
        price *= 0.50
elif room_type == "president apartment":
    price = p_president
    if nights < 10:
        price *= 0.90
    elif 10 >= nights <= 15:
        price *= 0.85
    elif nights > 15:
        price *= 0.80
if review == "positive":
    price *= 1.25
elif review == "negative":
    price *= 0.90

final_price = nights * price
print(f"{final_price:.2f}")
'''