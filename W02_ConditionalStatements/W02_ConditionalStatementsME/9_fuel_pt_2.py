fuel_type = str(input())
quantity = float(input())
club_cart = str(input())

price = 0

if fuel_type == "Gasoline" and club_cart == "Yes":
    price = 2.22 - 0.18
elif fuel_type == "Gasoline" and club_cart == "No":
    price = 2.22
elif fuel_type == "Diesel" and club_cart == "Yes":
    price = 2.33 - 0.12
elif fuel_type == "Diesel" and club_cart == "No":
    price = 2.33
elif fuel_type == "Gas" and club_cart == "Yes":
    price = 0.93 - 0.08
elif fuel_type == "Gas" and club_cart == "No":
    price = 0.93

final_price = quantity * price

if 20 <= quantity <= 25:
    final_price -= final_price * 0.08
elif quantity > 25:
    final_price -= final_price * 0.10

print(f"{final_price:.2f} lv.")

