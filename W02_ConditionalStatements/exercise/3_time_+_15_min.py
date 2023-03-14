hours = int(input())
minutes = int(input())
minutes += 15

hours += minutes // 60
minutes %= 60

if hours == 24:
    hours = 0

print(f"{hours}:{minutes:02d}")
