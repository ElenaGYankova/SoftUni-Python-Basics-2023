from math import ceil
number_of_easter_breads = int(input())
one_pack_sugar = 950
one_pack_flour = 750
total_sugar_used, total_flour_used, max_sugar_used, max_flour_used = 0, 0, 0, 0
for easter_bread in range(number_of_easter_breads):
    sugar_used = int(input())
    flour_used = int(input())
    total_sugar_used += sugar_used
    total_flour_used += flour_used
    if sugar_used > max_sugar_used:
        max_sugar_used = sugar_used
    if flour_used > max_flour_used:
        max_flour_used = flour_used

packs_sugar = ceil(total_sugar_used / one_pack_sugar)
packs_flour = ceil(total_flour_used / one_pack_flour)

print(f"Sugar: {packs_sugar}")
print(f"Flour: {packs_flour}")
print(f"Max used flour is {max_flour_used} grams, max used sugar is {max_sugar_used} grams.")

'''
from math import ceil

easter_bread_count = int(input())

total_sugar_used, total_flour_used = 0, 0
max_sugar_used, max_flour_used = 0, 0
for _ in range(easter_bread_count):
    current_sugar_used = int(input())
    current_flour_used = int(input())

    if current_sugar_used > max_sugar_used:
        max_sugar_used = current_sugar_used
    if current_flour_used > max_flour_used:
        max_flour_used = current_flour_used

    total_sugar_used += current_sugar_used
    total_flour_used += current_flour_used

sugar_packs = ceil(total_sugar_used / 950)
flour_packs = ceil(total_flour_used / 750)

print(f"Sugar: {sugar_packs}\n"
      f"Flour: {flour_packs}\n"
      f"Max used flour is {max_flour_used} grams, max used sugar is {max_sugar_used} grams.")
'''
