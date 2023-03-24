season_type = input()
group_type = input()
students_count = int(input())
nights_count = int(input())

if season_type == "Winter":
    if group_type == "girls":
        price = 9.60
        sport = "Gymnastics"
    elif group_type == "boys":
        price = 9.60
        sport = "Judo"
    elif group_type == "mixed":
        price = 10
        sport = "Ski"
if season_type == "Spring":
    if group_type == "girls":
        price = 7.20
        sport = "Athletics"
    elif group_type == "boys":
        price = 7.20
        sport = "Tennis"
    elif group_type == "mixed":
        price = 9.50
        sport = "Cycling"
if season_type == "Summer":
    if group_type == "girls":
        price = 15
        sport = "Volleyball"
    elif group_type == "boys":
        price = 15
        sport = "Football"
    elif group_type == "mixed":
        price = 20
        sport = "Swimming"

total = students_count * nights_count * price

if students_count >= 50:
    total *= 0.50
elif 20 <= students_count < 50:
    total *= 0.85
elif 10 <= students_count < 20:
    total *= 0.95

print(f"{sport} {total:.2f} lv.")
