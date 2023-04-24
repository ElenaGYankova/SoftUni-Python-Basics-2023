country = input()
discipline = input()

difficulty = 0
performance = 0
if country == "Russia":
    if discipline == "ribbon":
        difficulty = 9.100
        performance = 9.400
    elif discipline == "hoop":
        difficulty = 9.300
        performance = 9.800
    elif discipline == "rope":
        difficulty = 9.600
        performance = 9.000
elif country == "Bulgaria":
    if discipline == "ribbon":
        difficulty = 9.600
        performance = 9.400
    elif discipline == "hoop":
        difficulty = 9.550
        performance = 9.750
    elif discipline == "rope":
        difficulty = 9.500
        performance = 9.400
elif country == "Italy":
    if discipline == "ribbon":
        difficulty = 9.200
        performance = 9.500
    elif discipline == "hoop":
        difficulty = 9.450
        performance = 9.350
    elif discipline == "rope":
        difficulty = 9.700
        performance = 9.150

overall = difficulty + performance

to_max_needed = 100 * (1 - overall / 20)

print(f"The team of {country} get {overall:.3f} on {discipline}.\n"
      f"{to_max_needed:.2f}%")
