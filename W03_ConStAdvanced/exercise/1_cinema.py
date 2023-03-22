type = input()
rows = int(input())
columns = int(input())
income = 0

cinema_capacity = rows * columns

if type == "Premiere":
    income = cinema_capacity * 12.00
elif type == "Normal":
    income = cinema_capacity * 7.50
elif type == "Discount":
    income = cinema_capacity * 5.00

print(f"{income:.2f} leva")
