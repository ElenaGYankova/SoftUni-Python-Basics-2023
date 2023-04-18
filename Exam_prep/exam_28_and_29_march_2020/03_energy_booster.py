fruit = input()
pack_size = input()
packs_count = int(input())

pack_price = 0
if fruit == "Watermelon":
    if pack_size == "small":
        pack_price = 56.00 * 2
    elif pack_size == "big":
        pack_price = 28.70 * 5
elif fruit == "Mango":
    if pack_size == "small":
        pack_price = 36.66 * 2
    elif pack_size == "big":
        pack_price = 19.60 * 5
elif fruit == "Pineapple":
    if pack_size == "small":
        pack_price = 42.10 * 2
    elif pack_size == "big":
        pack_price = 24.80 * 5
elif fruit == "Raspberry":
    if pack_size == "small":
        pack_price = 20.00 * 2
    elif pack_size == "big":
        pack_price = 15.20 * 5

total_price = pack_price * packs_count

if total_price < 400:
    pass
elif 400 <= total_price <= 1000:
    total_price -= 0.15 * total_price
else:
    total_price -= 0.5 * total_price

print(f"{total_price:.2f} lv.")
