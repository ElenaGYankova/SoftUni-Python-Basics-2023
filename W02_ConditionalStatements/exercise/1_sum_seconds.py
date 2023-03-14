first = int(input())
second = int(input())
third = int(input())

time = first + second + third

minutes = time // 60
seconds = time % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")

"""import math
from math import floor

first = int(input())
second = int(input())
third = int(input())

total_time = first + second + third

minutes = total_time // 60
seconds = total_time % 60
minutes = math.floor(minutes)

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")


print()"""