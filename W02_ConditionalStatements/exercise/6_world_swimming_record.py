from math import floor
record = float(input())
distance = float(input())
time_meter = float(input())

time = (distance * time_meter) + ((floor(distance / 15)) * 12.5)
difference = time - record
if record > time:
    print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")