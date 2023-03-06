price_vegetables = float(input())
price_fruits = float(input())
weight_vegetables = int(input())
weight_fruits = int(input())
profit = ((price_vegetables * weight_vegetables) + (price_fruits * weight_fruits)) / 1.94
print(f"{profit:.2f}")