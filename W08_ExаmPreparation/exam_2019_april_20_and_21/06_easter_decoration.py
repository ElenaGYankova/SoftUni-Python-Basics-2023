number_of_clients = int(input())

product_price = 0
total = 0
for client in range(number_of_clients):
    command = input()
    products_counter = 0
    client_total = 0
    while command != "Finish":
        type_of_product = command
        products_counter += 1
        if type_of_product == "basket":
            product_price = 1.5
        elif type_of_product == "wreath":
            product_price = 3.8
        elif type_of_product == "chocolate bunny":
            product_price = 7
        client_total += product_price
        command = input()
    if products_counter % 2 == 0:
        client_total -= client_total * 0.2
    total += client_total

    print(f"You purchased {products_counter} items for {client_total:.2f} leva.")
average_bill = total / number_of_clients
print(f"Average bill per client is: {average_bill:.2f} leva.")

'''
customers_count = int(input())

total_items_count = 0
total_items_cost = 0

for _ in range(customers_count):
    current_items_count = 0
    current_items_cost = 0
    while True:
        item = input()
        if item == "Finish":
            break
        elif item == "basket":
            current_items_cost += 1.50
        elif item == "wreath":
            current_items_cost += 3.80
        elif item == "chocolate bunny":
            current_items_cost += 7.00
        current_items_count += 1

    if current_items_count % 2 == 0:
        current_items_cost -= 0.20 * current_items_cost
    print(f"You purchased {current_items_count} items for {current_items_cost:.2f} leva.")
    total_items_count += current_items_count
    total_items_cost += current_items_cost

average_items_cost = total_items_cost / customers_count
print(f"Average bill per client is: {average_items_cost:.2f} leva.")

'''