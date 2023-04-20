bag_over_20_kg = float(input())
bag_weight = float(input())
days_due_travel = int(input())
bags_count = int(input())

current_bag_price = 0
if bag_weight < 10:
    current_bag_price = 0.20 * bag_over_20_kg
elif bag_weight <= 20:
    current_bag_price = 0.50 * bag_over_20_kg
else:
    current_bag_price = bag_over_20_kg

if days_due_travel < 7:
    current_bag_price *= 1.40
elif days_due_travel <= 30:
    current_bag_price *= 1.15
else:
    current_bag_price *= 1.10

total = bags_count * current_bag_price

print(f"The total price of bags is: {total:.2f} lv.")
