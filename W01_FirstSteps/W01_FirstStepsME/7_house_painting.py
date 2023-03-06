x = float(input())
y = float(input())
h = float(input())
x_walls = (x * x) * 2 - (1.2 * 2)
y_walls = (x * y) * 2 - (1.5 * 1.5) * 2
roof = (x * y) * 2 + ((x * h) / 2) * 2
green_paint = (x_walls + y_walls) / 3.4
red_paint = roof / 4.3
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")