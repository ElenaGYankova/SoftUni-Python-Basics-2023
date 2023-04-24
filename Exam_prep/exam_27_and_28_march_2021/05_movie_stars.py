budget_for_actors = float(input())

command = input()
while not command == "ACTION" and budget_for_actors > 0:
    actor_name = command
    actor_salary = 0.20 * budget_for_actors
    if len(actor_name) <= 15:
        actor_salary = float(input())

    budget_for_actors -= actor_salary
    command = input()

if budget_for_actors >= 0:
    print(f"We are left with {budget_for_actors:.2f} leva.")
else:
    print(f"We need {abs(budget_for_actors):.2f} leva for our actors.")
