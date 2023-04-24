food_in_kg = int(input())
bought_food_grams = food_in_kg * 1000

food_eaten = 0
while food_eaten != "Adopted":
    food_eaten = int(food_eaten)
    bought_food_grams -= food_eaten

    food_eaten = input()

if bought_food_grams < 0:
    print(f"Food is not enough. You need {abs(bought_food_grams)} grams more.")
else:
    print(f"Food is enough! Leftovers: {abs(bought_food_grams)} grams.")
