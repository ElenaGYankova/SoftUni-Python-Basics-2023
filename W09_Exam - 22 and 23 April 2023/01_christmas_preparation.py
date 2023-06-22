wrapping_paper = int(input())
fabric = int(input())
glue = float(input())
discount = int(input())

total_sum = wrapping_paper * 5.8 + fabric * 7.2 + glue * 1.2
total_sum -= total_sum * discount / 100

print(f'{total_sum:.3f}')
