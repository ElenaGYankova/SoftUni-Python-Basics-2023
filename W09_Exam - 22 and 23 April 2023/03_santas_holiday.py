days = int(input())
room_type = input()
review = input()
price_for_night = 0

if days < 10:
    if room_type == "room for one person":
        price_for_night = 18
    elif room_type == "apartment":
        price_for_night = 25 * 0.70
    else:
        price_for_night = 35 * 0.90
elif 10 <= days <= 15:
    if room_type == "room for one person":
        price_for_night = 18
    elif room_type == "apartment":
        price_for_night = 25 * 0.65
    else:
        price_for_night = 35 * 0.85
else:
    if room_type == "room for one person":
        price_for_night = 18
    elif room_type == "apartment":
        price_for_night = 25 * 0.50
    else:
        price_for_night = 35 * 0.80

total_price = (days - 1) * price_for_night

if review == "positive":
    total_price *= 1.25
else:
    total_price *= 0.90

print(f'{total_price:.2f}')
