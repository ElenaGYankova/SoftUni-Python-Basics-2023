budget = float(input())
series_count = int(input())

for _ in range(series_count):
    series_title = input()
    series_price = float(input())
    if series_title == "Thrones":
        series_price -= 0.5 * series_price
    elif series_title == "Lucifer":
        series_price -= 0.4 * series_price
    elif series_title == "Protector":
        series_price -= 0.3 * series_price
    elif series_title == "TotalDrama":
        series_price -= 0.2 * series_price
    elif series_title == "Area":
        series_price -= 0.1 * series_price

    budget -= series_price

if budget >= 0:
    print(f"You bought all the series and left with {budget:.2f} lv.")
else:
    print(f"You need {abs(budget):.2f} lv. more to buy the series!")
