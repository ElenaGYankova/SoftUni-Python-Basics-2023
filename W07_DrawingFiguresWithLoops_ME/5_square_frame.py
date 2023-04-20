n = int(input())
print(f"+ {'- ' * (n - 2)}+")
for a in range(n - 2):
    print(f"| {'- ' * (n - 2)}|")
print(f"+ {'- ' * (n - 2)}+")
