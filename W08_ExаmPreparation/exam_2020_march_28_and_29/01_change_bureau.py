bitcoin_count = int(input())
yuan_count = float(input())
commission = float(input())

bitcoin_lev = bitcoin_count * 1168
yuan_dollar = yuan_count * 0.15
yuan_lev = yuan_dollar * 1.76

lev_total = bitcoin_lev + yuan_lev
euro_total = lev_total / 1.95
euro_total -= commission * euro_total / 100

print(f"{euro_total:.2f}")
