from math import floor
hours_needed = int(input())
days_available = int(input())
overtime_workers = int(input())
education = days_available * 0.1
overtime = days_available * overtime_workers * 2
total_time = floor(overtime + ((days_available - education) * 8))
difference = hours_needed - total_time
if total_time >= hours_needed:
    print(f"Yes!{floor(abs(difference))} hours left.")
else:
    print(f"Not enough time!{floor(difference)} hours needed.")