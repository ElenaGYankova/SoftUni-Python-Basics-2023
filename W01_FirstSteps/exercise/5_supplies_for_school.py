pen_package = int(input())
marker_package = int(input())
detergent = int(input())
discount = float(input())

supplies = (pen_package * 5.80) + (marker_package * 7.20) + (detergent * 1.20)
total = supplies - (supplies * discount / 100)
print(total)