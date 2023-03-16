day_off = int(input())

playtime = ((365 - day_off) * 63) + (day_off * 127)
diff = abs(30000 - playtime)
hours = diff // 60
minutes = diff % 60

if playtime > 30000:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
