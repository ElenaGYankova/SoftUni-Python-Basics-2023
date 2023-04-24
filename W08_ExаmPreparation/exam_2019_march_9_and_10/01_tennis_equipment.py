from math import floor, ceil

rocket_price = float(input())
rocket_count = float(input())
sneakers_count = float(input())

sneakers_price = rocket_price / 6

rockets_cost = rocket_count * rocket_price
sneakers_cost = sneakers_count * sneakers_price

equipment_cost = 0.20 * (rockets_cost + sneakers_cost)

total_cost = rockets_cost + sneakers_cost + equipment_cost

print(f"Price to be paid by Djokovic {floor(total_cost / 8)}\n"
      f"Price to be paid by sponsors {ceil(7 * total_cost / 8)}")
