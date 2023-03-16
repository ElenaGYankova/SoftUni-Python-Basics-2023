from math import floor, ceil

x_vineyards = int(input())
y_grapes = float(input())
z_liters_wine = int(input())
workers = int(input())

wine = ((x_vineyards * y_grapes) / 2.5 ) * 0.4
diff = abs(wine - z_liters_wine)
liters_per_person = diff / workers

if wine >= z_liters_wine:
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(liters_per_person)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
