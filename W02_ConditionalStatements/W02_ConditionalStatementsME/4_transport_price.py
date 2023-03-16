count_km = int(input())
day_night = str(input())

if day_night == "day":
    taxi_price = 0.7 + count_km * 0.79
else:
    taxi_price = 0.7 + count_km * 0.9

if count_km >= 20:
    bus_price = count_km * 0.09
if count_km >= 100:
    train_price = count_km * 0.06

if count_km < 20:
    print(f"{taxi_price:.2f}")
elif 20 <= count_km and count_km < 100 and bus_price > taxi_price:
    print(f"{taxi_price:.2f}")
elif 20 <= count_km and count_km < 100 and bus_price < taxi_price:
    print(f"{bus_price:.2f}")
elif 20 <= count_km and count_km >= 100 and bus_price > taxi_price and taxi_price < train_price:
    print(f"{taxi_price:.2f}")
elif 20 <= count_km and count_km >= 100 and taxi_price > bus_price and bus_price < train_price:
    print(f"{bus_price:.2f}")
else:
    print(f"{train_price:.2f}")
