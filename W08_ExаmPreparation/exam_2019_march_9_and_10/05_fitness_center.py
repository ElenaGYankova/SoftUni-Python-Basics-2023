visitors_count = int(input())

back_training, chest_training, legs_training = 0, 0, 0
abs_training, shake_count, bar_count = 0, 0, 0
activity_counter = 0
for n in range(visitors_count):
    activity = input()
    if activity == "Back":
        back_training += 1
    elif activity == "Chest":
        chest_training += 1
    elif activity == "Legs":
        legs_training += 1
    elif activity == "Abs":
        abs_training += 1
    elif activity == "Protein shake":
        shake_count += 1
    elif activity == "Protein bar":
        bar_count += 1

    if activity != "Protein shake" and activity != "Protein bar":
        activity_counter += 1

activity_percentage = 100 * activity_counter / visitors_count
consumers_percentage = 100 * (visitors_count - activity_counter) / visitors_count

print(f"{back_training} - back\n"
      f"{chest_training} - chest\n"
      f"{legs_training} - legs\n"
      f"{abs_training} - abs\n"
      f"{shake_count} - protein shake\n"
      f"{bar_count} - protein bar\n"
      f"{activity_percentage:.2f}% - work out\n"
      f"{consumers_percentage:.2f}% - protein")
