cargo = int(input())
bus = 0
truck = 0
train = 0
price = 0
quantity = 0

for i in range(cargo):
    tons = int(input())
    if tons <= 3:
        bus += tons
        price += tons * 200
        quantity += tons
    elif tons <= 11:
        truck += tons
        price += tons * 175
        quantity += tons
    elif tons >= 12:
        train += tons
        price += tons * 120
        quantity += tons

average_price = price / quantity
bus_average = (bus / quantity) * 100
truck_average = (truck / quantity) * 100
train_average = (train / quantity) * 100

print(f"{average_price:.2f}")
print(f"{bus_average:.2f}%")
print(f"{truck_average:.2f}%")
print(f"{train_average:.2f}%")
