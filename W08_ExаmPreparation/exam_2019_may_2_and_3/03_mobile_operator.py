contract_term = input()
contract_type = input()
mobile_internet = input()
due_months = int(input())

tax = 0
if contract_type == "Small":
    if contract_term == "one":
        tax = 9.98
    elif contract_term == "two":
        tax = 8.58
elif contract_type == "Middle":
    if contract_term == "one":
        tax = 18.99
    elif contract_term == "two":
        tax = 17.09
elif contract_type == "Large":
    if contract_term == "one":
        tax = 25.98
    elif contract_term == "two":
        tax = 23.59
elif contract_type == "ExtraLarge":
    if contract_term == "one":
        tax = 35.99
    elif contract_term == "two":
        tax = 31.79

if mobile_internet == "yes":
    if tax <= 10:
        tax += 5.50
    elif tax <= 30:
        tax += 4.35
    else:
        tax += 3.85

if contract_term == "two":
    tax -= 0.0375 * tax

tax_total = tax * due_months

print(f"{tax_total:.2f} lv.")
