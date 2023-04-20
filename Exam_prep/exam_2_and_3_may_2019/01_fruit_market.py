strawberries_price = float(input())
bananas = float(input())
oranges = float(input())
raspberries = float(input())
strawberries = float(input())

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price - (raspberries_price * 0.4)
bananas_price = raspberries_price - (raspberries_price * 0.8)

needed_money = strawberries * strawberries_price + bananas * bananas_price + oranges * oranges_price + \
               raspberries * raspberries_price
print(f"{needed_money:.2f}")