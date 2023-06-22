pocket_money = float(input())
profit_for_day = float(input())
expenses = float(input())
gift_price = float(input())

money_earned = (pocket_money * 5) + (profit_for_day * 5)
total_money = money_earned - expenses

if total_money > gift_price:
    print(f"Profit: {total_money:.2f} BGN, the gift has been purchased.")
else:
    diff = gift_price - total_money
    print(f"Insufficient money: {diff:.2f} BGN.")
