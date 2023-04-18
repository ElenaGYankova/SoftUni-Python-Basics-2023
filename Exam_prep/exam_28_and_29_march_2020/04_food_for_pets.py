count_days = int(input())
food = float(input())

dog_food_total, cat_food_total, cookies_total, food_total = 0, 0, 0, 0
for count_days in range(1, count_days + 1):
    dog_food = int(input())
    dog_food_total += dog_food

    cat_food = int(input())
    cat_food_total += cat_food

    food_for_day = dog_food + cat_food

    if count_days % 3 == 0:
        cookies = food_for_day * 0.10
        cookies_total += cookies

    food_total += food_for_day

food_percent, dog_percent, cat_percent = 0, 0, 0
if food > 0:
    food_percent = 100 * food_total / food
    dog_percent = 100 * dog_food_total / food_total
    cat_percent = 100 * cat_food_total / food_total

print(f"Total eaten biscuits: {round(cookies_total)}gr.")
print(f"{food_percent:.2f}% of the food has been eaten.")
print(f"{dog_percent:.2f}% eaten from the dog.")
print(f"{cat_percent:.2f}% eaten from the cat.")
