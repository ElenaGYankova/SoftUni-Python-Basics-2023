from math import floor, ceil

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cactus = int(input())
gift_price = float(input())

income = magnolias * 3.25 + hyacinths * 4 + roses * 3.5 + cactus * 8
total = income - (income * 0.05)
diff = abs(total - gift_price)
if total >= gift_price:
    print(f"She is left with {floor(diff)} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")
