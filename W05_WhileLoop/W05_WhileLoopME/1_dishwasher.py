detergent = int(input()) * 750
detergent_needed = 0
counter = 0
pot = 0
plate = 0

command = input()
while command != "End":
    dishes = int(command)
    if dishes == int(command):
        counter += 1

    if counter % 3 == 0:
        pot += dishes
        detergent_needed += dishes * 15

    else:
        plate += dishes
        detergent_needed += dishes * 5

    if detergent_needed > detergent:
        break

    command = input()

diff = abs(detergent - detergent_needed)
if detergent_needed <= detergent:
    print("Detergent was enough!")
    print(f"{plate} dishes and {pot} pots were washed.")
    print(f"Leftover detergent {diff} ml.")
else:
    print(f"Not enough detergent, {diff} ml. more necessary!")


#
#
# detergent_washing_dishes = int(input())
#
# bottle = 750
# one_dish = 5
# one_pot = 15
#
# total_preparation = detergent_washing_dishes * bottle
# dishes_count = 0
# pot_count = 0
# total_dishes_wash = 0
# total_pot_wash = 0
# washed_dishes = 0
# washed_pots = 0
# while True:
#     if total_preparation < 0:
#         print(f"Not enough detergent, {abs(total_preparation)} ml. more necessary!")
#         break
#     items_insert_in_dish_washer = input()
#     if items_insert_in_dish_washer == "End":
#         print(f"Detergent was enough!\n{total_dishes_wash} dishes and {total_pot_wash} "
#               f"pots were washed.\nLeftover detergent {total_preparation} ml.")
#         break
#     items_insert_in_dish_washer = int(items_insert_in_dish_washer)
#     dishes_count += 1
#     if dishes_count <= 2:
#         total_dishes_wash += items_insert_in_dish_washer
#         washed_dishes = total_preparation - (items_insert_in_dish_washer * one_dish)
#         total_preparation = washed_dishes
#         if washed_dishes > total_preparation:
#             total = total_preparation - washed_dishes
#             print(f"Not enough detergent, {total} ml. more necessary!")
#     else:
#         total_pot_wash += items_insert_in_dish_washer
#         pot_count += items_insert_in_dish_washer
#         washed_pots = total_preparation - (items_insert_in_dish_washer * one_pot)
#         total_preparation = washed_pots
#         dishes_count = 0








# number_detergents = int(input())
# total_detergents = number_detergents * 750
# command = input()
# counter = 0
# pots = 0
# dishes = 0
# needed_detergent = 0
# detergent_is_finished = False
#
# while command != "End":
#
#     total_dishes = int(command)
#     counter += 1
#     if counter % 3 == 0:
#         pots += total_dishes
#         needed_detergent += total_dishes * 15
#     else:
#         dishes += total_dishes
#         needed_detergent += total_dishes * 5
#     if needed_detergent > total_detergents:
#         detergent_is_finished = True
#         break
#     command = input()
#
# difference = abs(needed_detergent - total_detergents)
#
# if detergent_is_finished:
#     print(f"Not enough detergent, {difference} ml. more necessary!")
# else:
#     print("Detergent was enough!")
#     print(f"{dishes} dishes and {pots} pots were washed.")
#     print(f"Leftover detergent {difference} ml.")
#
#




#
# number_detergents = int(input())
# total_detergents = number_detergents * 750
# command = input()
# counter = 0
# pots = 0
# dishes = 0
# needed_detergent = 0
# detergent_is_finished = False
#
# while command != "End":
#     if needed_detergent > total_detergents:
#         detergent_is_finished = True
#         break
#     total_dishes = int(command)
#     counter += 1
#     if counter % 3 == 0:
#         pots += total_dishes
#         total_detergents -= total_dishes * 15
#     else:
#         dishes += total_dishes
#         total_detergents -= total_dishes * 5
#     if total_detergents < 0:
#         detergent_is_finished = True
#         break
#     command = input()
#
# difference = abs(needed_detergent - total_detergents)
#
# if detergent_is_finished:
#     print(f"Not enough detergent, {difference} ml. more necessary!")
# else:
#     print("Detergent was enough!")
#     print(f"{dishes} dishes and {pots} pots were washed.")
#     print(f"Leftover detergent {difference} ml.")
#



#
# number_of_detergent_bottles = int(input())
# command = input()
# volume_of_one_bottle_detergent = 750        # ml
# detergent_per_plate = 5                     # ml
# detergent_per_pot = 15                      # ml
# detergent_is_enough = False
# cycle_counter = 1
# count_plates = 0
# count_pots = 0
# available_detergent = number_of_detergent_bottles * volume_of_one_bottle_detergent
# # from the console you read number of detergent bottles
# # On each subsequent line, until the command "End" or until the amount of detergent is exhausted -
# # number of dishes to be washed - an integer in the range [1… 100]
# while command != "End":
#     number_dishes = int(command)
#     if cycle_counter % 3 == 0:
#         count_pots += number_dishes
#         available_detergent -= (detergent_per_pot * number_dishes)
#     else:
#         count_plates += number_dishes
#         available_detergent -= (detergent_per_plate * number_dishes)
#     if available_detergent < 0:
#         break
#     command = input()
#     cycle_counter += 1
# if available_detergent >= 0:
#     detergent_is_enough = True
# if detergent_is_enough:
#     print("Detergent was enough!")
#     print(f"{count_plates} dishes and {count_pots} pots were washed.")
#     print(f"Leftover detergent {available_detergent} ml.")
# else:
#     print(f"Not enough detergent, {abs(available_detergent)} ml. more necessary!")
#


