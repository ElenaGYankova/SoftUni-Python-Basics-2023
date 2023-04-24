budget = float(input())

total_spend = 0
products_bought = 0
counter = 0
while True:
    product_name = input()
    if product_name == "Stop":
        print(f"You bought {products_bought} products for {total_spend:.2f} leva.")
        break
    counter += 1
    product_price = float(input())
    if counter % 3 == 0:
        product_price /= 2
    if budget - product_price < 0:
        print(f"You don't have enough money!")
        print(f"You need {product_price - budget:.2f} leva!")
        break

    budget -= product_price
    total_spend += product_price
    products_bought += 1
