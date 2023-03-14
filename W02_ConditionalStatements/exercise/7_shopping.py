budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

price_v = video_cards * 250
price_p = price_v * 0.35
price_r = price_v * 0.10
final_price = price_v + (processors * price_p) + (ram * price_r)

if video_cards > processors:
    final_price *= 0.85
diff = abs(budget - final_price)

if final_price <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
