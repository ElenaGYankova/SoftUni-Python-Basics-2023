month = input()
nights_count = int(input())

studio = 0
apartment = 0
if month in "May" "October":
    studio = 50
    apartment = 65
    if 7 < nights_count <= 14:
        studio *= 0.95
    elif nights_count > 14:
        studio *= 0.70
        apartment *= 0.90
if month in "June" "September":
    studio = 75.2
    apartment = 68.7
    if nights_count > 14:
        studio *= 0.80
        apartment *= 0.90
if month in "July" "August":
    studio = 76
    apartment = 77
    if nights_count > 14:
        apartment *= 0.90
studio_price = studio * nights_count
apartment_price = apartment * nights_count

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
