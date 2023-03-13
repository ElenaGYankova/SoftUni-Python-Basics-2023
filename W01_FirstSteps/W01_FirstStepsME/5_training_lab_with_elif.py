w = float(input())
h = float(input())
if(h < 3):
    print("Hall too small")
elif(w < h):
    print("Hall too small")
elif(w > 100):
    print("Hall too big")
workplaces_column = w // 1.2
workplaces_row = (h - 1) // 0.7
corridor = 1 * w
workplaces = workplaces_column * workplaces_row - 3
print(int(workplaces))
