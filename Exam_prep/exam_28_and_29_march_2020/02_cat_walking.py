walk_duration = int(input())
walks_count = int(input())
calories = int(input())

calories_burned = walks_count * walk_duration * 5

balance = calories_burned - calories / 2

if balance >= 0:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")
