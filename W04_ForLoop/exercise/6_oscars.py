actors_name = input()
academy_points = float(input())
n_graders = int(input())
final_points = academy_points

for i in range(n_graders):
    grader_name = input()
    grader_points = float(input())
    final_points += (len(grader_name) * grader_points) / 2
    if final_points > 1250.5:
        print(f"Congratulations, {actors_name} got a nominee for leading role with {final_points:.1f}!")
        break
diff = 1250.5 - final_points
if final_points <= 1250.5:
    print(f"Sorry, {actors_name} you need {diff:.1f} more!")
