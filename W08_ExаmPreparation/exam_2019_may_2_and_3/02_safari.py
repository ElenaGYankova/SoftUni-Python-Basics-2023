budget = float(input())
fuel = float(input())
day_of_week = input()

expenses = (fuel * 2.10) + 100
discount = 0
if day_of_week == "Saturday":
    discount = 0.10
elif day_of_week == "Sunday":
    discount = 0.20

total = expenses - (expenses * discount)
diff = abs(total - budget)

if budget > total:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")
