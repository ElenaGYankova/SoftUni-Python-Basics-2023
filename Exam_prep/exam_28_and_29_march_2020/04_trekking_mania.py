# https://judge.softuni.org/Contests/Practice/Index/2275#7

group_count = int(input())

climbers_total = 0
musala, monblan, kilimanjaro, k2, everest = 0, 0, 0, 0, 0
for _ in range(group_count):
    climbers_count = int(input())
    if climbers_count <= 5:
        musala += climbers_count
    elif climbers_count <= 12:
        monblan += climbers_count
    elif climbers_count <= 25:
        kilimanjaro += climbers_count
    elif climbers_count <= 40:
        k2 += climbers_count
    else:
        everest += climbers_count

    climbers_total += climbers_count

musala_percent = 100 * musala / climbers_total
monblan_percent = 100 * monblan / climbers_total
kilimanjaro_percent = 100 * kilimanjaro / climbers_total
k2_percent = 100 * k2 / climbers_total
everest_percent = 100 * everest / climbers_total

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
