from math import ceil

workout_days = int(input())
km_for_day = float(input())

total_km = km_for_day
for day in range(workout_days):
    speed_km = int(input())
    km_for_day *= ((speed_km / 100) + 1)
    total_km += km_for_day

diff = abs(1000 - total_km)
if total_km > 1000:
    print(f"You've done a great job running {ceil(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers")
