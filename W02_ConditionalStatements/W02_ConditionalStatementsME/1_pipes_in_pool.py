volume_litres = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

percent = volume_litres / 100

full = (h * p1 + h * p2) / percent
volume_percent = (h * p1 + h * p2) / 100
pipe_1 = p1 * h / volume_percent
pipe_2 = p2 * h / volume_percent

diff = h * p1 + h * p2
left = diff - volume_litres

if volume_litres >= diff:
    print(f"The pool is {full:.2f}% full. Pipe 1: {pipe_1:.2f}%. Pipe 2: {pipe_2:.2f}%.")
else:
    print(f"For {h} hours the pool overflows with {left:.2f} liters.")
