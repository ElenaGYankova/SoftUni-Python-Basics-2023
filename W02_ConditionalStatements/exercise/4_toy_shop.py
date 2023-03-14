trip = float(input())
puzzle = int(input())
talking_doll = int(input())
teddy_bear = int(input())
minion = int(input())
truck = int(input())
discount = 0

total_price = puzzle * 2.60 + talking_doll * 3 + teddy_bear * 4.10 + minion * 8.20 + truck * 2
total_toys = puzzle + talking_doll + teddy_bear + minion + truck

if total_toys >= 50:
    total_price *= 0.75

rent = total_price * 0.10
profit = total_price - rent

expenses = abs(profit - trip)

if profit >= trip:
    print(f"Yes! {expenses:.2f} lv left.")
else:
    print(f"Not enough money! {expenses:.2f} lv needed.")
