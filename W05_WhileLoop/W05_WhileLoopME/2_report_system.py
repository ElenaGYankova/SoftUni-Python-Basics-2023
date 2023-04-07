expected_sum = int(input())
payment_type = 0 # като 1 е плащане с кеш, а 2 е плащане с карта
cash_payment = 0
card_payment = 0

cash_count = 0
card_count = 0
command = input()
while command != "End":
    payment_type += 1
    product_price = int(command)
    if product_price > 100 and payment_type == 1:
        print("Error in transaction!")
    elif product_price <= 10 and payment_type == 2:
        print("Error in transaction!")

    if product_price <= 100 and payment_type == 1:
        cash_payment += product_price
        cash_count += 1
        print("Product sold!")
    elif product_price > 10 and payment_type == 2:
        card_payment += product_price
        card_count += 1
        print("Product sold!")

    total_payment = card_payment + cash_payment
    if total_payment >= expected_sum:
        print(f"Average CS: {cash_payment / cash_count:.2f}")
        print(f"Average CC: {card_payment / card_count:.2f}")
        break

    if payment_type == 2:
        payment_type = 0

    command = input()

else:
    print("Failed to collect required money for charity.")



# expected_sum = int(input())
#
# cash_payment = 0
# card_payment = 0
# total_items = 0
# sum_left = expected_sum
# card_count = 0
# cash_count = 0
#
# while True:
#     total_sum = cash_payment + card_payment
#     if total_sum >= expected_sum:
#         cash_payment = cash_payment / cash_count
#         card_payment = card_payment / card_count
#         print(f"Average CS: {cash_payment:.2f}\nAverage CC: {card_payment:.2f}")
#         break
#     sum_to_be_colected = input()
#     if sum_to_be_colected == "End":
#         print("Failed to collect required money for charity.")
#         break
#     sum_to_be_colected = int(sum_to_be_colected)
#     total_items += sum_to_be_colected
#     if sum_to_be_colected <= 100:
#         sum_left += + sum_to_be_colected
#         cash_payment += sum_to_be_colected
#         cash_count += 1
#         print("Product sold!")
#     else:
#         print(f"Error in transaction!")
#     sum_to_be_colected = input()
#     if sum_to_be_colected == "End":
#         print("Failed to collect required money for charity.")
#         break
#     sum_to_be_colected = int(sum_to_be_colected)
#     if sum_to_be_colected <= 10:
#         print(f"Error in transaction!")
#     else:
#         sum_left += + sum_to_be_colected
#         card_payment += +sum_to_be_colected
#         card_count += 1
#         print("Product sold!")
