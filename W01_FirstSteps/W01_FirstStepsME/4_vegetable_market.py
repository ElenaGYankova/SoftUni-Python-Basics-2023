vegetables_kg = float(input())
fruits_kg = float(input())
total_vegetables = int(input())
total_fruits = int(input())
# * 1.94
total = ((vegetables_kg * total_vegetables) + (fruits_kg * total_fruits)) / 1.94
print(f"{total:.2f}")
