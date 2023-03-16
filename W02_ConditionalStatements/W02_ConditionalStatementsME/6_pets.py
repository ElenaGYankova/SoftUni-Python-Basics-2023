from math import floor, ceil

count_days = int(input())
food_kg = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_gr = float(input())

needed_food = (count_days * dog_food_kg) + (count_days * cat_food_kg) + \
              ((count_days * turtle_food_gr) / 1000)
diff = abs(food_kg - needed_food)

if food_kg > needed_food:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")
