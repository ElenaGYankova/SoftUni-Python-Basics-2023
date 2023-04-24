checkpoint_minutes = int(input())
checkpoint_seconds = int(input())
chute_length = float(input())
time_per_100m = int(input())

checkpoint_time = checkpoint_minutes * 60 + checkpoint_seconds

speed = time_per_100m / 100
slope_advantage_time = chute_length / 120 * 2.5

quota_time = chute_length * speed - slope_advantage_time

time_balance = quota_time - checkpoint_time
if time_balance > 0:
    print(f"No, Marin failed! He was {time_balance:.3f} second slower.")
else:
    print(f"Marin Bangiev won an Olympic quota!\n"
          f"His time is {quota_time:.3f}.")
