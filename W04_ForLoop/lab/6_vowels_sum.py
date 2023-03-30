text = input()
sum = 0

for i in range(0, len(text)):
    if text[i] == "a":
        sum += 1   #sum_of_points = sum_of_points + 1
    if text[i] == "e":
        sum += 2
    if text[i] == "i":
        sum += 3
    if text[i] == "o":
        sum += 4
    if text[i] == "u":
        sum += 5

print(sum)
