capacity = float(input())

count_suitcase = 0
free_space = capacity
suitcase_volume = float(input())
while suitcase_volume != "End":
    count_suitcase += 1
    suitcase_volume = float(suitcase_volume)

    if count_suitcase % 3 == 0:
        suitcase_volume += 0.10 * suitcase_volume

    if free_space < suitcase_volume:
        print("No more space!")
        count_suitcase -= 1
        break

    free_space -= suitcase_volume
    suitcase_volume = input()
else:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {count_suitcase} suitcases loaded.")
