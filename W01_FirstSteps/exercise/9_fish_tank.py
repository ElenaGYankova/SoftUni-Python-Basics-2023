length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = int(input())

litres = (length_cm * width_cm * height_cm) / 1000
occupied = percent / 100
needed_litres = litres * (1 - occupied)

print(needed_litres)