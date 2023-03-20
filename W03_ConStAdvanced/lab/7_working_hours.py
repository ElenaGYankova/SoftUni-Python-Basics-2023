hours = int(input())
day = input()

if 10 > hours or hours > 18 or day == "Sunday":
    print("closed")
else:
    print("open")