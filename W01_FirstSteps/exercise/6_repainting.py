nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())
price_matts = nylon * 1.50 + paint * 14.50 + thinner * 5 + 3 + 0.40 + ((paint * 10 / 100) * 14.50)
price_work = (price_matts * 30 / 100) * hours
price_final = price_work + price_matts
print(price_final)