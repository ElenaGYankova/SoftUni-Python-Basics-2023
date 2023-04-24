sweet_breads = int(input())
egg_cartons = int(input())
cookies_kilos = int(input())

sweet_breads_cost = sweet_breads * 3.20
eggs_cost = egg_cartons * 4.35
cookies_cost = cookies_kilos * 5.40
egg_painting = egg_cartons * 12 * 0.15

total_cost = sweet_breads_cost + eggs_cost + cookies_cost + egg_painting

print(f"{total_cost:.2f}")
