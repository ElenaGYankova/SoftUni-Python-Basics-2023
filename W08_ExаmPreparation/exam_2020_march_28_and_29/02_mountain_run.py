record_time = float(input())
distance = float(input())
speed = float(input())

climbing_time = distance * speed
delay_time = (distance // 50) * 30
total_time = climbing_time + delay_time
slower = total_time - record_time

if total_time < record_time:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {slower:.2f} seconds slower.")
