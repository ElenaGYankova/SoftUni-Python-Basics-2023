change = float(input())
coins_change = round(change * 100)

count_coins = 0
while coins_change > 0:
    if coins_change >= 200:
        coins_change -= 200
    elif coins_change >= 100:
        coins_change -= 100
    elif coins_change >= 50:
        coins_change -= 50
    elif coins_change >= 20:
        coins_change -= 20
    elif coins_change >= 10:
        coins_change -= 10
    elif coins_change >= 5:
        coins_change -= 5
    elif coins_change >= 2:
        coins_change -= 2
    elif coins_change >= 1:
        coins_change -= 1
    count_coins += 1
print(count_coins)
