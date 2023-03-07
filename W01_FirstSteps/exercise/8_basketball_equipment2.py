sum_for_year = int(input())

sneakers = sum_for_year - (sum_for_year * 0.4)
clothes = sneakers - (sneakers * 0.2)
ball_price = clothes - (clothes * 0.75)
accessories = ball_price - (ball_price * 0.80)

total = sum_for_year + sneakers + clothes + ball_price + accessories
print(total)
