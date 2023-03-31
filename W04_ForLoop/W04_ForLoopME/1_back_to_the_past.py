inheritance = float(input())
year_to_live = int(input())
money = 0

for years in range(1800, year_to_live + 1, 1):
    if years % 2 == 0:
        money += 12000
    else:
        money += 12000 + 50 * ((18 + years) - 1800)
diff = abs(inheritance - money)
if inheritance >= money:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")
