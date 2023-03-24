x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

condition_1 = (x == x1 or x == x2) and (y1 <= y and y <= y2)
condition_2 = (y == y1 or y == y2) and (x1 <= x and x <= x2)

if condition_1 or condition_2:
    print("Border")
else:
    print("Inside / Outside")
