minutes_walking = int(input())
walking_for_day = int(input())
calories = int(input())

total_walking_minutes = walking_for_day * minutes_walking
total_burned_calories = total_walking_minutes * 5
if total_burned_calories >= calories / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burned_calories}.")
