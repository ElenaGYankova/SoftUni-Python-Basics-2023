day = int(input())
hours_per_day = int(input())

tax = 0
for current_day in range(1, day + 1):
    daily_tax = 0
    for hour in range(1, hours_per_day + 1):
        hour_cost = 1.00
        if current_day % 2 == 0 and hour % 2 != 0:
            hour_cost = 2.50
        if current_day % 2 != 0 and hour % 2 == 0:
            hour_cost = 1.25

        daily_tax += hour_cost
    tax += daily_tax
    print(f"Day: {current_day} - {daily_tax:.2f} leva")

print(f"Total: {tax:.2f} leva")
