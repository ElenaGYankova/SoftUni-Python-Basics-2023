movie_budget = float(input())
destination = input()
season = input()
movie_days = int(input())

shooting_day_cost = None
if destination == "Dubai":
    if season == "Winter":
        shooting_day_cost = 45000
    elif season == "Summer":
        shooting_day_cost = 40000

elif destination == "Sofia":
    if season == "Winter":
        shooting_day_cost = 17000
    elif season == "Summer":
        shooting_day_cost = 12500

elif destination == "London":
    if season == "Winter":
        shooting_day_cost = 24000
    elif season == "Summer":
        shooting_day_cost = 20250

total_price = movie_days * shooting_day_cost

if destination == "Dubai":
    total_price -= 0.30 * total_price
elif destination == "Sofia":
    total_price += 0.25 * total_price

if movie_budget >= total_price:
    print(f"The budget for the movie is enough! We have {movie_budget - total_price:.2f} leva left!")
else:
    print(f"The director needs {total_price - movie_budget:.2f} leva more!")
