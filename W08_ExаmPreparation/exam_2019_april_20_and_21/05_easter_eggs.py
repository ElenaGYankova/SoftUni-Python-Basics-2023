number_of_eggs = int(input())

red_eggs, orange_eggs, blue_eggs, green_eggs,  = 0, 0, 0, 0
max_color = ''
for egg in range(number_of_eggs):
    egg_color = input()
    if egg_color == "red":
        red_eggs += 1
    elif egg_color == "orange":
        orange_eggs += 1
    elif egg_color == "blue":
        blue_eggs += 1
    elif egg_color == "green":
        green_eggs += 1
max_eggs = 0
if red_eggs > max_eggs:
    max_eggs = red_eggs
    max_color = "red"
if orange_eggs > max_eggs:
    max_eggs = orange_eggs
    max_color = "orange"
if blue_eggs > max_eggs:
    max_eggs = blue_eggs
    max_color = "blue"
if green_eggs > max_eggs:
    max_eggs = green_eggs
    max_color = "green"

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_eggs} -> {max_color}")

'''
eggs_count = int(input())

max_colour = ''
max_count = -1
red, orange, blue, green = 0, 0, 0, 0
for _ in range(eggs_count):
    egg_colour = input()
    if egg_colour == "red":
        red += 1
    elif egg_colour == "orange":
        orange += 1
    elif egg_colour == "blue":
        blue += 1
    elif egg_colour == "green":
        green += 1

    if red > max_count:
        max_count = red
        max_colour = egg_colour
    elif orange > max_count:
        max_count = orange
        max_colour = egg_colour
    elif blue > max_count:
        max_count = blue
        max_colour = egg_colour
    elif green > max_count:
        max_count = green
        max_colour = egg_colour

print(f"Red eggs: {red}\n"
      f"Orange eggs: {orange}\n"
      f"Blue eggs: {blue}\n"
      f"Green eggs: {green}\n"
      f"Max eggs: {max_count} -> {max_colour}")
'''