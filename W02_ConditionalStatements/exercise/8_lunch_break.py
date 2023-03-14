from math import ceil

series_name = str(input())
duration = int(input())
lunch_break = int(input())

lunch = lunch_break / 8
chill = lunch_break / 4

total_time = duration + lunch + chill
free_time = abs(lunch_break - total_time)

if lunch_break >= total_time:
    print(f"You have enough time to watch {series_name} and left with {ceil(free_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(free_time)} more minutes.")
