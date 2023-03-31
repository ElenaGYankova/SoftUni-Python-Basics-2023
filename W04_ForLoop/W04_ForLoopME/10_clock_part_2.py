hour = 23
minutes = 59
seconds = 59

for i in range(hour + 1):
    for m in range(minutes + 1):
        for s in range(seconds + 1):
            print(f"{i} : {m} : {s}")
