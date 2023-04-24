number_of_guests = int(input())
price_per_guest = float(input())
budget = float(input())

if 10 <= number_of_guests <= 15:
    price_per_guest -= price_per_guest * 0.15
elif 15 < number_of_guests <= 20:
    price_per_guest -= price_per_guest * 0.2
elif number_of_guests > 20:
    price_per_guest -= price_per_guest * 0.25

cake_price = budget * 0.1

total = number_of_guests * price_per_guest + cake_price
difference = abs(total - budget)
if total <= budget:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")

'''
guests_count = int(input())
envelope_price = float(input())
budget = float(input())

cake_cost = 0.10 * budget

discount = 0
if guests_count < 10:
    pass
elif guests_count <= 15:
    discount = 0.15
elif guests_count <= 20:
    discount = 0.20
else:
    discount = 0.25

envelope_cost = (1 - discount) * envelope_price * guests_count

total_cost = envelope_cost + cake_cost

balance = budget - total_cost

if balance > 0:
    print(f"It is party time! {balance:.2f} leva left.")
else:
    print(f"No party! {abs(balance):.2f} leva needed.")
'''