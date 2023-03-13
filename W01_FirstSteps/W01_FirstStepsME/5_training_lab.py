w_meters = float(input())
h_meters = float(input())

w = w_meters * 100
h = h_meters * 100
row = w // 120
desk = (h - 100) // 70
total = (desk * row) - 3

print(int(total))
