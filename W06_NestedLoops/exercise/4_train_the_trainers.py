jury = int(input())

avg_presentation = 0
total_presentations = 0
avg_course = 0
course_finished = False

while not course_finished:
    presentation_name = input()

    if presentation_name == "Finish":
        course_finished = True
        break
    total_presentations += 1
    for n in range(1, jury + 1):
        grade = float(input())
        avg_presentation += grade

    avg_presentation = avg_presentation / jury
    print(f"{presentation_name} - {avg_presentation:.2f}.")
    avg_course += avg_presentation
    avg_presentation = 0

if course_finished:
    avg_course = avg_course / total_presentations
    print(f"Student's final assessment is {avg_course:.2f}.")
