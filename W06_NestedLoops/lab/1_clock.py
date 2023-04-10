# hours = (0, 23 + 1) or (0, 24)
# minutes = (0, 59 + 1) or (0, 60)

for hours in range(24):
    for minutes in range(60):
        print(f"{hours}:{minutes}")

''' ако искаме да добавим второ число 0 към часовника:
for hours in range(24):
    for minutes in range(60):
        print(f"{hours:02d}:{minutes:02d}") '''

'''
hour = 24
minute = 60
for i in range(hour):
    for m in range(minute):
        print(f"{i}:{m}") '''