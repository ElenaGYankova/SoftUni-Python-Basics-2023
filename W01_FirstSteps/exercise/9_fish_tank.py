length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = float(input())
litres = length_cm * width_cm * height_cm / 1000
real_litres = litres - (litres * percent / 100)
print(real_litres)