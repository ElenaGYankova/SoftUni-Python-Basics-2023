student_name = input()
current_class = 1
total_grade = 0
fail = 0
is_excluded = False

while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        fail += 1
        if fail > 1:
            is_excluded = True
            break
    else: # elif current_grade >= 4:
        current_class += 1
        total_grade += current_grade
if is_excluded:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    average_grade = total_grade / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
