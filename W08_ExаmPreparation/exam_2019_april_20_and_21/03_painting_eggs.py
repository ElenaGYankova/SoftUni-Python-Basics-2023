batch_type = input()
eggs_color = input()
batches_count = int(input())

batch_price = 0
if batch_type == "Large":
    if eggs_color == "Red":
        batch_price = 16
    elif eggs_color == "Green":
        batch_price = 12
    elif eggs_color == "Yellow":
        batch_price = 9
elif batch_type == "Medium":
    if eggs_color == "Red":
        batch_price = 13
    elif eggs_color == "Green":
        batch_price = 9
    elif eggs_color == "Yellow":
        batch_price = 7
elif batch_type == "Small":
    if eggs_color == "Red":
        batch_price = 9
    elif eggs_color == "Green":
        batch_price = 8
    elif eggs_color == "Yellow":
        batch_price = 5

total_profit = batches_count * batch_price
neto_profit = (1 - 0.35) * total_profit

print(f"{neto_profit:.2f} leva.")
