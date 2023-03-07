nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours = int(input())

supplies = ((nylon_needed + 2) * 1.50 + (paint_needed + (paint_needed * 0.10))
            * 14.50 + (thinner_needed * 5.00)) + 0.40
workers = (supplies * 0.3) * hours
print(supplies + workers)