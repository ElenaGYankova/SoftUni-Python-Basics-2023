flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
egg_cartons = int(input())
yeast = int(input())

sugar_price = flour_price - (flour_price * 0.25)
egg_carton_price = flour_price + (flour_price * 0.1)
yeast_price = sugar_price - (sugar_price * 0.8)

total = flour_kg * flour_price + sugar_kg * sugar_price + yeast * yeast_price + egg_cartons * egg_carton_price

print(f"{total:.2f}")

'''
flour_price = float(input())
flour_kilos = float(input())
sugar_kilos = float(input())
egg_packs = int(input())
leaven_packs = int(input())

sugar_price = (1 - 0.25) * flour_price
egg_pack_price = (1 + 0.10) * flour_price
leaven_pack_price = (1 - 0.80) * sugar_price

flour_cost = flour_kilos * flour_price
sugar_cost = sugar_kilos * sugar_price
eggs_cost = egg_packs * egg_pack_price
leven_cost = leaven_packs * leaven_pack_price

total_cost = flour_cost + sugar_cost + eggs_cost + leven_cost

print(f"{total_cost:.2f}")
'''