days = int(input())
hours = int(input())

price = 0
total = 0
for a in range(1, days + 1):
    for b in range(1, hours + 1):
        if a % 2 == 0 and b % 2 != 0:
            price += 2.5
        elif a % 2 != 0 and b % 2 == 0:
            price += 1.25
        else:
            price += 1
    print(f"Day: {a} - {price:.2f} leva")
    total += price
    price = 0
print(f"Total: {total:.2f} leva")
