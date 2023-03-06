basketball_tax = int(input())
sneakers = basketball_tax - (basketball_tax * 40 / 100)
shirt = sneakers - (sneakers * 20 / 100)
ball = shirt / 4
accesories = ball / 5
sum = basketball_tax + sneakers + shirt + ball + accesories
print(sum)
