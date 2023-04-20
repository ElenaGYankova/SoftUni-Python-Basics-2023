joinery_count = int(input())
type_joinery = input()
delivery = input()
is_invalid_order = False

total = 0
if joinery_count < 10:
    is_invalid_order = True

else:
    price_joinery = 0
    if type_joinery == "90X130":
        price_joinery = 110
        if joinery_count > 60:
            price_joinery -= 0.08 * price_joinery
        elif joinery_count > 30:
            price_joinery -= 0.05 * price_joinery

    elif type_joinery == "100X150":
        price_joinery = 140
        if joinery_count > 80:
            price_joinery -= 0.10 * price_joinery
        elif joinery_count > 40:
            price_joinery -= 0.06 * price_joinery

    elif type_joinery == "130X180":
        price_joinery = 190
        if joinery_count > 50:
            price_joinery -= 0.12 * price_joinery
        elif joinery_count > 20:
            price_joinery -= 0.07 * price_joinery

    elif type_joinery == "200X300":
        price_joinery = 250
        if joinery_count > 50:
            price_joinery -= 0.14 * price_joinery
        elif joinery_count > 25:
            price_joinery -= 0.09 * price_joinery

    else:
        is_invalid_order = True

    total = price_joinery * joinery_count

    if delivery == "With delivery":
        total += 60
    elif delivery == "Without delivery":
        pass
    else:
        is_invalid_order = True

    if joinery_count > 99:
        total -= 0.04 * total

if is_invalid_order:
    print("Invalid order")
else:
    print(f"{total:.2f} BGN")
