from math import pi
area_of_figures = str(input())

if area_of_figures == "square":
    side_a = float(input())
    area = side_a * side_a
    print(f"{area:.3f}")
elif area_of_figures == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = (side_a + side_b) * 2
    print(f"{area:.3f}")
elif area_of_figures == "circle":
    side_a = float(input())
    area = side_a * side_a * pi
    print(f"{area:.3f}")
elif area_of_figures == "triangle":
    side_a = float(input())
    side_b = float(input())
    area = (side_a * side_b) / 2
    print(f"{area:.3f}")
